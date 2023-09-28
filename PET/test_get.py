import pytest
import requests
import json

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/1"
    response_get = requests.get(url)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 1
    assert response_get.json()['status'] == "OK"

def test_get_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet/12345"
    response_get = requests.get(url)
    print("response =", response_get.json())
    assert response_get.json()['message'] == "Pet not found"