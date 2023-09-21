import requests
import pytest
import json

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/1"
    response = requests.get(url,verify=False)
    print("result = ", response)
