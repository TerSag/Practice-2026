import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

print("--- ВИКОНАННЯ GET-ЗАПИТУ ---")
response_get = requests.get(url + "/1")

print(f"Статус-код: {response_get.status_code}")
print("Заголовки відповіді:")
print(f" Content-Type: {response_get.headers.get('Content-Type')}")
print(f" Date: {response_get.headers.get('Date')}")

print("\nТіло відповіді (JSON):")
print(response_get.json())

print("\n" + "="*40 + "\n")

print("--- ВИКОНАННЯ POST-ЗАПИТУ ---")
payload = {
    "title": "Мій новий пост",
    "body": "Це текст повідомлення, надісланий через Python.",
    "userId": 1
}

response_post = requests.post(url, json=payload)

print(f"Статус-код: {response_post.status_code} (Створено)")
print("Тіло відповіді сервера:")
print(response_post.json())