from http.client import responses

import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture
def user_data():
   return {
    "id": 1000,
    "username": "FlyffiUpdate",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }


def test_user_createUser_post(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200

def test_user_get(user_data):
    username = user_data["username"]
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert user_data.get("username") == user_data["username"]

def test_user_put(user_data):
    user_data = user_data.copy()
    username = user_data["username"]
    user_data["username"] = "FlyffiUpdate"
    response = requests.put(f"{BASE_URL}/user/{username}", json=user_data, headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("message") == str(user_data["id"])


def test_user_delete(user_data):
    username = user_data["username"]
    response = requests.delete(f"{BASE_URL}/user/{username}", headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 404, f"code: {response.status_code}"


def test_user_get_login(user_data):
    response = requests.get(f"{BASE_URL}/user/login", headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200

def test_user_get_logout(user_data):
    response = requests.get(f"{BASE_URL}/user/logout", headers=HEADERS)
    assert response.status_code == 200, f"code: {response.status_code}"
    response_data = response.json() if response.content else {}
    assert response_data.get("code") == 200
