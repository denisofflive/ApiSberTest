import requests
from resources import urls


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
