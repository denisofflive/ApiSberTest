import requests
import pytest
import resources.urls as urls
from Steps import support_steps as support_steps
from Steps import generate_json_steps as generate_json_steps
from Steps import request_steps as request_steps
from Steps import assert_steps as assert_steps
import pytest
import allure

# Тест создания нового питомца
@allure.step
@pytest.mark.smoke_API
@pytest.mark.pet
@pytest.mark.parametrize('type',
                         [
                             generate_json_steps.create_json_post_pet_required_params(),
                             generate_json_steps.create_json_post_pet_all_params()
                         ],
                         ids=["required_param", "all_param"]
                         )
def test_post_pet(type):
    # Создание JSON с передаваемым типом
    request = type
    # Отправка запроса
    request_post = request_steps.request_post(urls.url_pet_post, request)
    print("result = ", request_post.json())
    # Проверяем что id не пустой конструкцией is not None
    assert_steps.assert_not_none_id(request_post)
    # Проверка через GET, что объект действительно создан
    request_get = request_steps.request_get(urls.url_pet_get_id(str(request_post.json()['id'])))
    # Проверка, что по данному ID возвращается первоначально созданный объект
    assert_steps.assert_equals_response_ids(request_post, request_get)
    return request_post

# Негативный тест создания нового питомца
@allure.step
@pytest.mark.smoke_API
@pytest.mark.pet

def test_post_pet_negative():
    # Создание JSON c отсутствующим параметром (request['category']['name'] =)
    request = generate_json_steps.create_json_post_pet_required_fields()
    request['name'] = []
    # Отправка запроса
    request_post = request_steps.request_post(urls.url_pet_post, request)
    print("result = ", request_post.json())
    # Проверяем ответ
    assert_steps.assert_equals_response_value(request_post, 'message', 'something bad happened')

# Тест проверки существования животного с заданным id
@pytest.mark.smoke_API
@pytest.mark.pet
def test_get_pet():
    # Создадим животное
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_post_pet_all_params())
    # Отправляем запрос на проверку животного с id созданного животного
    response_get = request_steps.request_get(urls.url_pet_get_id(str(response_post.json()['id'])))
    # Выводим ответ
    print("response =", response_get.json())
    # Анализируем ответ
    assert_steps.assert_equals_response_value(response_get, "id", str(response_post.json()['id']))
    assert_steps.assert_equals_response_value(response_get, "status", "sold")

# Негативный тест проверки существования животного с заданным id
@pytest.mark.smoke_API
@pytest.mark.pet
def test_get_pet_negative():
    # Формируем URL c не существующим ID
    print(urls.url_get)
    # проверяем ответ
    response_get = request_steps.request_get(urls.url_get)
    print(response_get)
    # Проверяем, что такой страницы (пользователя) не существует
    assert_steps.assert_page_not_found(response_get)

# Тест изменения животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_put_pet():
    # Создадим животное с заданным ID
    response_post = test_post_pet(generate_json_steps.create_json_post_pet_all_params())
    # Анализируем ответ
    assert_steps.assert_not_none_id(response_post)
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_pet_put(str(response_post.json()['id']))
    # Выполним PUT
    response_put = request_steps.request_put(urls.url_pet_post, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'photoUrls', '[]')

# Негативный тест изменения животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_put_pet_id_negative():
    # Задаем ID животного
    id = support_steps.generate_random_letter_strings(5)
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_pet_put(id)
    # Выполним PUT
    response_put = request_steps.request_put(urls.url_pet_post, request)
    # Проверяем ответ
    assert_steps.assert_equals_response_value(response_put, 'message', 'something bad happened')

# Тест удаления животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_delete_pet():
    # Отправляем запрос
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_post_pet_all_params())
    # Формируем URL удаления
    url_delete = urls.url_pet_post + "/" + str(response_post.json()['id'])
    # Удаляем пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверяем код ответа
    assert_steps.assert_equals_response_value(response_delete, 'code', '200')
    # Делаем запрос с ID удаленного животного
    response_get = request_steps.request_get(url_delete)
    # Проверяем, что животное удалено
    assert_steps.assert_equals_response_value(response_get, 'message', 'Pet not found')

# Негативный тест удаления животного
@pytest.mark.smoke_API
@pytest.mark.pet
def test_delete_pet_id_negative():
    # Формируем URL c не существующим ID для удаления
    url_delete = urls.url_pet_post + "/" + support_steps.generate_random_number_strings(5)
    # Удаляем пользователя
    response_delete = request_steps.delete_user(url_delete)
    # Проверяем, что такой страницы (пользователя) не существует
    assert_steps.assert_page_not_found(response_delete)

# тест поиска животного по статусу
@pytest.mark.smoke_API
@pytest.mark.pet
def test_get_pet_by_status():
    # Создадим животное
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_post_pet_all_params())
    # Анализируем ответ
    assert_steps.assert_not_none_id(response_post)
    # Проверим есть ли животное с нужным статусом
    response_get = request_steps.request_get(urls.url_pet_findbystatus("sold"))
    print("response =", response_get.json())
    assert_steps.assert_status_sold(response_get)

# Негативный тест поиска животного по несуществующему статусу
@pytest.mark.smoke_API
@pytest.mark.pet
def test_get_pet_by_status_negative():
    # Создадим животное
    response_post = request_steps.request_post(urls.url_pet_post, generate_json_steps.create_json_post_pet_all_params())
    # Анализируем ответ
    assert_steps.assert_not_none_id(response_post)
    # Проверим есть ли животное с несуществующим статусом
    response_get = request_steps.request_get(urls.url_pet_findbystatus("negative"))
    print("response =", response_get.json())
    assert_steps.assert_status_not_found(response_get)

def test_post_pet_id_uploadImage():
    # Открываем фаил
    fp = open('../files/send.txt')
    files = {'file': fp}
    # Формируем запрос
    response = requests.post(urls.url_pet_post_uploadimage('2'), files=files)
    fp.close()
    print(response.text)
    # Проверяем запрос
    response_get = requests.get(urls.url_pet_get_id('1'))
    print("response =", response_get.json())
    # Проверяем ответ
    assert_steps.assert_id_1(response_get)
