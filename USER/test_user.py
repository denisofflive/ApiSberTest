import requests
import resources.urls as urls

def test_post_create_user():
    request = {}
    request["id"] = 777555
    request["username"] = "Denzel"
    request["firstName"] = "Denis"
    request["lastName"] = "Denisov"
    request["email"] = "denzel@sber.net"
    request["password"] = "777555"
    request["phone"] = "iphone"
    request["userStatus"] = 0
    print(request)

    response_post = requests.post(urls.url_pet_user, json=request, verify=False)
    print("result = ", response_post.json())

    assert response_post.json()['code'] == 200


def test_get_user():
    username = "Denzel"
    url_get = urls.url_pet_user + "/" + username
    response_get = requests.get(url_get)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 777555
    assert response_get.json()['userStatus'] == 0


def test_put_user():
    request = {}
    request["id"] = 777555
    request["username"] = "Denzel"
    request["firstName"] = "Denis"
    request["lastName"] = "Denisov"
    request["email"] = "denzel@sber.net"
    request["password"] = "777555"
    request["phone"] = "android"
    request["userStatus"] = 0

    print(request)
    url_put = urls.url_pet_user + "/" + str(request['username'])
    print("url_put =", url_put)
    response_post = requests.put(url_put, json=request, verify=False)
    print("result = ", response_post.json())

    response_get = requests.get(url_put)
    print("response =", response_get.json())

    assert response_get.json()['id'] == 777555


def test_delete_user():
    username = "Denzel"
    url_delete = urls.url_pet_user + "/" + username
    print("URL_delete", url_delete)

    response_delete = requests.delete(url_delete, verify=False)
    print("response =", response_delete.json())

    response_get = requests.get(url_delete, verify=False)
    print("response =", response_get.json())

    assert response_get.json()['message'] == 'User not found'
