import requests
import pytest

def test_post_petstore():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberCat'
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    print("request = ", request)

    request_post = requests.post(url, json=request, verify=False)
    print("result = ", request_post.json())

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/9223372036854775807"
    request_get = requests.get(url, verify=False)
    print("result =", request_get.json())
