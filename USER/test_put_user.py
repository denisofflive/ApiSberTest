import requests
import resources.urls as urls

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
    print("response =", response_get.json())

    assert response_get.json()['id'] == 777555
