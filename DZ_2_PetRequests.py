import requests
import resources.urls as urls


"""
Домашнее задание
1. Покройте тестами оставшиеся методы раздела Pet
2. Покройте тестами часть проекта по разделу User для методов:
POST/user, PUT/user/{username}, GET/user/{username}, DELETE/user/{username}

https://petstore.swagger.io/

"""

# GET pet FindStatus
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
    url = "https://petstore.swagger.io/v2/pet/"
    request = {'id': 1}
    url_post = url + str(request['id']) + "/uploadImage"
    print("url_post =", url_post)
    fp = open('send.txt', 'rb')
    files = {'file': fp}
    resp = requests.post(url_post, files=files)
    fp.close()
    print(resp.text)

    url_get = url + str(request['id'])
    response_get = requests.get(url_get)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 1
    assert response_get.json()['status'] == "OK"

# POST/user Create User

def test_post_create_user():
    url = "https://petstore.swagger.io/v2/user"

    request = {"id": 777555,
               "username": "Denzel",
               "firstName": "Denis",
               "lastName": "Denisov",
               "email": "denzel@sber.net",
               "password": "777555",
               "phone": "iphone",
               "userStatus": 0}

    print(request)
    response_post = requests.post(url, json=request, verify=False)
    print("result = ", response_post.json())


# GET/user  Username
def test_get_user():
    url = "https://petstore.swagger.io/v2/user"
    userName = "Denzel"
    url_get = url + "/" + userName
    response_get = requests.get(url_get)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 777555
    assert response_get.json()['userStatus'] == 0

# PUT/user  Update user
def test_put_user():
    url = "https://petstore.swagger.io/v2/user/"
    request = {"id": 777555,
               "username": "Denzel",
               "firstName": "Denis",
               "lastName": "Denisov",
               "email": "denzel@sber.net",
               "password": "777555",
               "phone": "iphone",
               "userStatus": 0}

    print(request)
    url_put = url + str(request['username'])
    print("url_put =", url_put)
    response_post = requests.put(url_put, json=request, verify=False)
    print("result = ", response_post.json())

    response_get = requests.get(url_put)
    print("responce =", response_get.json())



# DELETE/user  Delete user
def test_delete_user():
    url = "https://petstore.swagger.io/v2/user/"
    userName = "Denzel"
    url_delete = url + "/" + userName
    print("URL_delete", url_delete)
    response_delete = requests.delete(url_delete)
    print("responce =", response_delete.json())

    response_get = requests.get(url_delete)
    print("responce =", response_get.json())
