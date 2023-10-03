import requests
import pytest
import json

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


