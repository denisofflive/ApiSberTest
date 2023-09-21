import requests
import pytest

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


def test_put_pet():
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberCat'
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    print(request)

    request_post = requests.post(url, json=request, verify=False)
    print("result post= ", request_post.json())

    request_put = {}
    request_put['id'] = str(request_post.json()['id'])
    request_put['name'] = "sberDog"
    request_put['photoUrls'] = ['photoSberDog']
    print('request put = ', request_put)

    request_put_r = requests.put(url, json=request_put, verify=False)
    print("result put=", request_put_r.json())

    assert request_put_r.json()['name'] == request_put['name']

    url_get = "https://petstore.swagger.io/v2/pet/" + str(request_post.json()['id'])
    request_get = requests.get(url_get, verify=False)

    assert request_get.json()['name'] == request_put['name']

def test_put_pet_negative():
    url = "https://petstore.swagger.io/v2/pet"

    request_put = {}
    request_put['id'] = []
    request_put['name'] = "sberDog"
    request_put['photoUrls'] = ['photoSberDog']
    print('request put = ', request_put)

    request_put_r = requests.put(url, json=request_put, verify=False)
    print("result put=", request_put_r.json())

    assert request_put_r.json()['message'] == 'something bad happened'

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
