import requests

LIST_COLORS_ENDPOINT = "http://127.0.0.1:8000/api/v1/colors/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/auth/"

response = requests.post(AUTH_ENDPOINT, json={"username": "test", "password": "test@123"})

if response.status_code == 200:
    token = response.json()["token"]
    print(token)
    headers = {"Authorization": "Token " + token}
    colors = requests.post(LIST_COLORS_ENDPOINT, headers=headers)
    print(colors.json())