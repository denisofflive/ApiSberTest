import pytest
import requests
import json
from resources import urls


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
    url = "https://petstore.swagger.io/v2/pet/9223372036854775797"
    response_get = requests.get(url)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 9223372036854775797


def test_get_pet_id_negative():
    url = "https://petstore.swagger.io/v2/pet/123456789"
    response_get = requests.get(url)
    print("response =", response_get.json())
    assert response_get.json()['message'] == "Pet not found"


def test_get_pet_findByStatus_available():
    response_get = requests.get(urls.url_pet_findbystatus("available"), verify=False)
    print("result =", response_get.json())

    assert response_get.json()[0]['status'] == 'available'

def test_get_pet_findByStatus_sold():
    response_get = requests.get(urls.url_pet_findbystatus("sold"), verify=False)
    print("result =", response_get.json())

    assert response_get.json()[0]['status'] == 'sold'


def test_get_pet_findByStatus_pending():
    response_get = requests.get(urls.url_pet_findbystatus("pending"), verify=False)
    print("result =", response_get.json())

    assert response_get.json()[0]['status'] == 'pending'


def test_get_pet_findByStatus_negative():
    response_get = requests.get(urls.url_pet_post + "/" + str(777777777), verify=False)
    print("result =", response_get.json())

    assert response_get.json()['message'] == "Pet not found"

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
