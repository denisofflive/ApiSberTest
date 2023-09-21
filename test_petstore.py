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


def test_put_pet():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberCat'
    request['category'] = {}
    request['category']['name'] = 'cats'
    request['photoUrls'] = ['photoSberCat']
    print(request)

    response_post = requests.post(url, json=request, verify=False)
    print("result = ", response_post.json())

    request_put = {}
    request_put['id'] = str(response_post.json()['id'])
    request_put['name'] = "sberWowKitten"
    print(request_put)
    response_put = requests.put(url, json=request_put)
    print("result =", response_put)

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
