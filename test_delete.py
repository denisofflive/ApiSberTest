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

