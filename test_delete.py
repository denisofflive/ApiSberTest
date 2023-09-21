import requests
import pytest
import json

def test_delete_pet():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberCat'
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    print("request = ", request)

    request_post = requests.post(url, json=request, verify=False)
    print("result = ", request_post.json())

    url_delete = "https://petstore.swagger.io/v2/pet/" + str(request_post.json()['id'])

    request_delete = requests.delete(url_delete, verify=False)
    print("result delete =", request_delete.json())

    assert request_delete.json()['code'] == 200


    request_get = requests.get(url_delete, verify=False)
    assert request_get.json()['message'] == 'Pet not found'


def test_delete_pet_negative():
    url_delete = "https://petstore.swagger.io/v2/pet" + "7777"

    request_delete = requests.delete(url_delete, verify=False)
    print("result delete =", request_delete)

    assert str(request_delete).__contains__("404")

