import requests


"""
Домашнее задание
1. Покройте тестами оставшиеся методы раздела Pet
2. Покройте тестами часть проекта по разделу User для методов:
POST/user, PUT/user/{username}, GET/user/{username}, DELETE/user/{username}

https://petstore.swagger.io/

"""

# GET pet FindStatus
def test_get_pet_findByStatus_available():
    url = "https://petstore.swagger.io/v2/pet/123"
    response_get = requests.get(url, verify=False)
    print("result =", response_get.json())

    assert response_get.json()['status'] == 'available'


def test_get_pet_findByStatus_available_nagetive():
    url = "https://petstore.swagger.io/v2/pet/" + str(777777777)
    response_get = requests.get(url, verify=False)
    print("result =", response_get.json())

    assert response_get.json()['message'] == "Pet not found"


def test_get_pet_findByStatus_sold():
    url = "https://petstore.swagger.io/v2/pet/131131"
    response_get = requests.get(url, verify=False)
    print("result =", response_get.json())

    assert response_get.json()['status'] == 'sold'


def test_get_pet_findByStatus_pending():
    url = "https://petstore.swagger.io/v2/pet/499"
    response_get = requests.get(url, verify=False)
    print("result =", response_get.json())

    assert response_get.json()['status'] == 'pending'

# POST petID

def test_post_pet_id():
    url = "https://petstore.swagger.io/v2/pet/"
    request = {'id': 123, 'name': 'Denis', 'status': 'disable'}
    print(request)

    response_post = requests.post(url, json=request, verify=False)
    print("result = ", response_post.json())

    """Проверяем что id не пустой конструкцией is not None"""
    assert response_post.json()['id'] is not None

    url_get = "https://petstore.swagger.io/v2/pet/" + str(response_post.json()['id'])
    print("url_get", url_get)

    response_get = requests.get(url_get)
    print("result get = ", response_get)

    assert response_get.json()['id'] == response_post.json()['id']
