from flask import Flask, jsonify, request

app = Flask(__name__)

# Імітація бази даних
users = [
    {"id": 1, "name": "Олександр", "email": "alex@example.com"},
    {"id": 2, "name": "Марія", "email": "maria@example.com"}
]

def format_response(status, data=None, message=""):
    """Універсальна функція для формування структури відповіді"""
    return jsonify({
        "status": status,
        "data": data,
        "message": message
    })

@app.route('/users', methods=['GET'])
def get_users():
    return format_response("success", users, "Список користувачів отримано")

@app.route('/users', methods=['POST'])
def create_user():
    new_data = request.json
    if not new_data or "name" not in new_data:
        return format_response("error", None, "Некоректні дані"), 400
    
    new_user = {
        "id": len(users) + 1,
        "name": new_data["name"],
        "email": new_data.get("email", "")
    }
    users.append(new_user)
    return format_response("success", new_user, "Користувача створено"), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return format_response("success", user, "Користувача знайдено")
    return format_response("error", None, "Користувача не знайдено"), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return format_response("error", None, "Користувача не знайдено"), 404
    
    update_data = request.json
    user.update(update_data)
    return format_response("success", user, "Дані оновлено")

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return format_response("error", None, "Користувача не знайдено"), 404
    
    users = [u for u in users if u["id"] != user_id]
    return format_response("success", None, f"Користувача з ID {user_id} видалено")

if __name__ == '__main__':
    app.run(debug=True, port=5000)