import requests
import resources.urls as urls
import Steps.support_steps as support_steps


def test_post_pet():
    request = {}
    request['id'] = 1
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'

    print("request = ", request)

    request_post = requests.post(urls.url_pet_post, json=request, verify=False)
    print("result = ", request_post.json())

    """Проверяем что id не пустой конструкцией is not None"""
    assert request_post.json()['id'] is not None

    request_get = requests.get(urls.url_pet_get_id(str(request_post.json()['id'])), verify=False)

    assert request_post.json()['id'] == request_get.json()['id']


def test_post_pet_negative():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = []

    print("request = ", request)

    request_post = requests.post(urls.url_pet_post, json=request, verify=False)
    print("result = ", request_post.json())

    assert request_post.json()['message'] == "something bad happened"


def test_get_pet():
    # Создаём запрос
    request = {}
    request['id'] = 1
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # Выводим запрос
    print("request = ", request)
    # Отправляем запрос
    request_post = requests.post(urls.url_pet_post, json=request, verify=False)
    # Выводим результат
    print("result = ", request_post.json())

    # Отправляем запрос на проверку животного с id созданного животного
    response_get = requests.get(urls.url_pet_get_id("1"))
    # Выводим ответ
    print("response =", response_get.json())
    # Сравниваем ответ
    assert response_get.json()['id'] == 1


def test_get_pet_id_negative():
    response_get = requests.get(urls.url_pet_get_id("123456789"))
    print("response =", response_get.json())
    assert response_get.json()['message'] == "Pet not found"


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


def test_put_pet():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    print(request)

    request_post = requests.post(urls.url_pet_post, json=request, verify=False)
    print("result post= ", request_post.json())

    request_put = {}
    request_put['id'] = str(request_post.json()['id'])
    request_put['name'] = support_steps.generate_random_letter_string(7)
    request_put['photoUrls'] = ['photoSberDog']
    print('request put = ', request_put)

    request_put_r = requests.put(urls.url_pet_post, json=request_put, verify=False)
    print("result put=", request_put_r.json())

    assert request_put_r.json()['name'] == request_put['name']

    request_get = requests.get(urls.url_pet_get_id(str(request_post.json()['id'])), verify=False)

    assert request_get.json()['name'] == request_put['name']


def test_put_pet_negative():
    request_put = {}
    request_put['id'] = []
    request_put['name'] = support_steps.generate_random_letter_string(7)
    request_put['photoUrls'] = ['photoSberDog']
    print('request put = ', request_put)

    request_put_r = requests.put(urls.url_pet_post, json=request_put, verify=False)
    print("result put=", request_put_r.json())

    assert request_put_r.json()['message'] == 'something bad happened'


def test_delete_pet():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = ['photoSberCat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    print("request = ", request)

    request_post = requests.post(urls.url_pet_post, json=request, verify=False)
    print("result = ", request_post.json())

    request_delete = requests.delete(urls.url_pet_get_id(str(request_post.json()['id'])), verify=False)
    print("result delete =", request_delete.json())

    assert request_delete.json()['code'] == 200

    request_get = requests.get(urls.url_pet_get_id(str(request_post.json()['id'])), verify=False)
    assert request_get.json()['message'] == 'Pet not found'


def test_delete_pet_negative():
    request_delete = requests.delete(urls.url_pet_get_id("7777"), verify=False)
    print("result delete =", request_delete)

    assert str(request_delete).__contains__("404")
