import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

if response.status_code == 200:
    
    data = response.json()

    
    print(data)

    for obj in data:
        print(obj['id'], obj['title'], obj['completed'])
else:
    print(f"Ошибка запроса. Статус код: {response.status_code}")