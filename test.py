import requests

url = 'http://127.0.0.1:8080/plan-activity'
data = {
    "latitude": "40.7128",
    "longitude": "-74.0060",
    "date": "2025-03-12"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

print(response.json())