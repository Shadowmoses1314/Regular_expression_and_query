import requests


def make_request(url, method, payload=None):
    if method.upper() == "GET":
        response = requests.get(url)
    elif method.upper() == "POST":
        response = requests.post(url, json=payload)
    else:
        raise ValueError("Invalid HTTP method. Supported methods: GET, POST")

    if not response.ok:
        raise ValueError(f"Status code: {response.status_code}")

    return response


url = "https://jsonplaceholder.typicode.com/posts"
method = "POST"
payload = {
    "title": "Test Title",
    "body": "Test Body",
    "userId": 1
}

response = make_request(url, method, payload)
print(response.status_code)
print(response.json())
