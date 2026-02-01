from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    db_url = os.getenv('DATABASE_URL')
    return f"Сервер працює! Підключення до БД: {db_url}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)