import requests
import pytest
import json


def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/9222968140497181246"
    request_get = requests.get(url, verify=False)
    print("result =", request_get.json())

    assert request_get.json()['id'] == 9222968140497181246

def test_get_pet_negative():
    url = "https://petstore.swagger.io/v2/pet/" + str(777777777)
    request_get = requests.get(url, verify=False)
    print("result =", request_get.json())

    assert request_get.json()['message'] == "Pet not found"
