import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

payload = {}
headers = {}

r = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(r.text)
print(data)

for obj in data:
    print(obj['id'], obj['title'], obj['completed'])