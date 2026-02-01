import os
from dotenv import load_dotenv

file_found = load_dotenv()

def connect_to_service():
    print("--- ДІАГНОСТИКА КОНФІГУРАЦІЇ ---")
    

    if not file_found:
        print("[Увага]: Файл .env не знайдено! Перевірте його наявність у папці.")
        return

    db_connection = os.getenv("DB_URL")
    api_token = os.getenv("API_KEY")
    debug_mode = os.getenv("DEBUG")

    print(f"Зчитано DB_URL: {db_connection}")
    
    if api_token:
        print(f"Зчитано API_KEY: {api_token[:5]}...****************")
    else:
        print("Зчитано API_KEY: None")

    print("-" * 30)


    if db_connection and api_token:
        print("[Успіх]: Конфігурація додатка завантажена успішно.")
        print(f"Режим налагодження (DEBUG): {debug_mode}")
    else:
        print("[Помилка]: Змінні в .env порожні або некоректні.")

if __name__ == "__main__":
    connect_to_service()