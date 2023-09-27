import requests


def fetch_api_data():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    return data["message"]
