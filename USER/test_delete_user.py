import requests


def test_delete_user():
    url = "https://petstore.swagger.io/v2/user/"
    username = "Denzel"
    url_delete = url + username
    print("URL_delete", url_delete)

    response_delete = requests.delete(url_delete, verify=False)
    print("response =", response_delete.json())

    response_get = requests.get(url_delete, verify=False)
    print("response =", response_get.json())

    assert response_get.json()['message'] == 'User not found'

