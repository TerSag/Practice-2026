from flask import Flask, request, jsonify
import jwt
import bcrypt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key' # Ключ для підпису JWT

users_db = {}

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users_db:
        return jsonify({"message": "Користувач вже існує"}), 400
    
    users_db[username] = hash_password(password)
    return jsonify({"message": "Користувача зареєстровано успішно"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    hashed_pw = users_db.get(username)
    if hashed_pw and check_password(password, hashed_pw):
        # Генерація токена на 30 хвилин
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({"token": token})
    
    return jsonify({"message": "Невірні дані"}), 401

@app.route('/profile', methods=['GET'])
def profile():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"message": "Токен відсутній"}), 401
    
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({
            "message": f"Вітаємо у профілі, {data['user']}!",
            "status": "Доступ дозволено"
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Термін дії токена вичерпано"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Невалідний токен"}), 401

if __name__ == '__main__':
    app.run(debug=True)