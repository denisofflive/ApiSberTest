import requests
import resources.urls as urls

def test_get_user():
    url = "https://petstore.swagger.io/v2/user"
    userName = "Denzel"
    url_get = url + "/" + userName
    response_get = requests.get(url_get)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 777555
    assert response_get.json()['userStatus'] == 0
