import requests


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

    assert response_post.json()['code'] == 200
