import pytest
import requests
from request_func import make_request


@pytest.fixture
def mock_get(monkeypatch):
    class MockResponse:
        def __init__(self, url):
            self.url = url
            self.ok = True
            self.status_code = 200
            self.json_data = {
                "message": "GET request successful"
            }

        def json(self):
            return self.json_data

    def mock_get_request(url):
        return MockResponse(url)

    monkeypatch.setattr(requests, 'get', mock_get_request)


@pytest.fixture
def mock_post(monkeypatch):
    class MockResponse:
        def __init__(self, url, payload):
            self.url = url
            self.ok = True
            self.status_code = 201
            self.json_data = {
                "message": f"POST request successful with payload: {payload}"
            }

        def json(self):
            return self.json_data

    def mock_post_request(url, json):
        return MockResponse(url, json)

    monkeypatch.setattr(requests, 'post', mock_post_request)


def test_make_request_get(mock_get):
    url = "https://examples.com"
    method = "GET"
    response = make_request(url, method)

    assert response.ok
    assert response.status_code == 200
    assert response.json() == {"message": "GET request successful"}


def test_make_request_post(mock_post):
    url = "https://exampless.com"
    method = "POST"
    payload = {"key": "value"}
    response = make_request(url, method, payload)

    assert response.ok
    assert response.status_code == 201
    assert response.json() == {
        "message": "POST request successful with payload: {'key': 'value'}"}


def test_make_request_invalid_method():
    url = "https://exam.com"
    method = "INVALID"

    with pytest.raises(ValueError) as e:
        make_request(url, method)

    assert str(e.value) == "Invalid HTTP method. Supported methods: GET, POST"


def test_make_request_failed_get(monkeypatch):
    def mock_failed_get_request(url):
        response = requests.Response()
        response.url = url
        response.status_code = 404
        return response

    monkeypatch.setattr(requests, 'get', mock_failed_get_request)

    url = "https://example.com"
    method = "GET"

    with pytest.raises(ValueError) as e:
        make_request(url, method)

    assert str(e.value) == "Status code: 404"


def test_make_request_failed_post(monkeypatch):
    def mock_failed_post_request(url, json):
        response = requests.Response()
        response.url = url
        response.status_code = 500
        return response

    monkeypatch.setattr(requests, 'post', mock_failed_post_request)

    url = "https://example.com"
    method = "POST"
    payload = {"key": "value"}

    with pytest.raises(ValueError) as e:
        make_request(url, method, payload)

    assert str(e.value) == "Status code: 500"
