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
    request = {'id': 1, 'name': 'Denis', 'status': 'disable'}
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

# POST uploadImage
def test_post_pet_id_uploadImage():
    url = "https://petstore.swagger.io/v2/pet"
    request = {'code': 1, 'type': 'DENZEL', 'message': 'additionalMetadata: DENZEL\nFile uploaded to ./denisov.jpg, 451937 bytes'}
    print(request)

    response_post = requests.post(url, json=request, verify=False)
    print("result = ", response_post.json())

    """Проверяем что id не пустой конструкцией is not None"""
    assert response_post.json()['id'] is not None

    url_get = "https://petstore.swagger.io/v2/pet/" + str(response_post.json()['id']) + str("/uploadImage")
    print("url_get", url_get)

    response_get = requests.get(url_get)
    print("result get = ", response_get)

    assert response_get.json()['id'] == response_post.json()['id']


# POST/user Create User

def test_post_create_user():
    url = "https://petstore.swagger.io/v2/user"
    # request = {}
    # request["id"] = 777555
    # request["username"] = "denzel"
    # request["firstName"] = "Denis"
    # request["lastName"] = "Denisov"
    # request["email"] = "denzel@sber.net"
    # request["password"] = "777555"
    # request["phone"] = "iphone"
    # request["userStatus"] = 1

    request = {"id": 777555,"username": "denzel","firstName": "Denis","lastName": "Denisov",
               "email": "denzel@sber.net","password": "777555","phone": "iphone","userStatus": 1}

    request_post = requests.post(url, json=request, verify=False)
    # print("request = ", request)
    print("result request_post.json = ", request_post.json())


    """Проверяем что id не пустой конструкцией is not None"""
    assert request_post.json()['message'] is not None

    url_get = "https://petstore.swagger.io/v2/user/denzel"
    request_get = requests.get(url_get, verify=False)
    print(request_get)

    assert request_get.json()['email'] == 'denzel@sber.net'

# GET/user  Username
def test_get_user():
    url = "https://petstore.swagger.io/v2/user/denzel"
    request_get = requests.get(url, verify=False)
    print("result =", request_get.json())

    assert request_get.json()['username'] == 'denzel'

# PUT/user  Update user
def test_put_user():
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request['id'] = 777555
    request['username'] = 'denzel'
    request['firstName'] = 'Denis'
    request['lastName'] = 'Denisov'
    request['email'] = 'denzel@sber.net'
    request['password'] = '777555'
    request['phone'] = 'iphone'
    request['userStatus'] = 1

    print(request)

    request_post = requests.post(url, json=request, verify=False)
    print("result post= ", request_post.json())

    request_put = {}
    request_put['username'] = "denzel moscow"
    print('request put = ', request_put)

    request_put_r = requests.put(url, json=request_put, verify=False)
    print("result put=", request_put_r.json())

    assert request_put_r.json()['username'] == request_put['username']

    url_get = "https://petstore.swagger.io/v2/user/" + str(request_post.json()['username'])
    request_get = requests.get(url_get, verify=False)

    assert request_get.json()['username'] == request_put['username']

# DELETE/user  Delete user
def test_delete_user():
    url = "https://petstore.swagger.io/v2/user/denzel"
    request = {}
    request['id'] = 777555
    request['username'] = 'denzel'
    request['firstName'] = 'Denis'
    request['lastName'] = 'Denisov'
    request['email'] = 'denzel@sber.net'
    request['password'] = '777555'
    request['phone'] = 'iphone'
    request['userStatus'] = 1

    print(request)

    request_post = requests.post(url, json=request, verify=False)
    print("result = ", request_post.json())

    url_delete = "https://petstore.swagger.io/v2/user/denzel"

    request_delete = requests.delete(url_delete, verify=False)
    print("result delete =", request_delete.json())

    assert request_delete.json()['code'] == 200


    request_get = requests.get(url_delete, verify=False)
    assert request_get.json()['message'] == 'User not found'