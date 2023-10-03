import requests
import pytest
import json

def test_post_pet():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberCat'
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    print("request = ", request)

    request_post = requests.post(url, json=request, verify=False)
    print("result = ", request_post.json())

    """Проверяем что id не пустой конструкцией is not None"""
    assert request_post.json()['id'] is not None

    url_get = "https://petstore.swagger.io/v2/pet/" + str(request_post.json()['id'])
    request_get = requests.get(url_get, verify=False)

    assert request_post.json()['id'] == request_get.json()['id']

def test_post_pet_negative():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberCat'
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = []
    print("request = ", request)

    request_post = requests.post(url, json=request, verify=False)
    print("result = ", request_post.json())

    assert request_post.json()['message'] == "something bad happened"



