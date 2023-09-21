import requests
import pytest
import json

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
