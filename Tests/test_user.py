import requests
import resources.urls as urls
import Steps.generate_json_steps as generate_json_steps
import Steps.request_steps as request_steps
import pytest


# Тест создания пользователя без указания имени
@pytest.mark.smoke_API
@pytest.mark.user
def test_post_user_runner():
    post_user('')


# Тест создания пользователя с указанием имени
@pytest.mark.smoke_API
@pytest.mark.user
def post_user(username):
    # Создаем JSON
    request = generate_json_steps.create_json_pet_user(username)
    # Отправляем запрос
    response_post = requests.post(urls.url_pet_user, json=request)
    # Выводим результат
    print("result = ", response_post.json())
    # Проверяем, что вернулся код ответа 200
    assert response_post.json()['code'] == 200
    # # Проверяем, что вернулся тип ответа unknown
    assert response_post.json()['type'] == 'unknown'


# Тест получения пользователя
@pytest.mark.smoke_API
@pytest.mark.user
def test_get_user():
    # Подготавливаем тестового пользователя
    post_user(urls.username)
    # Передаем запрос
    response_get = requests.get(urls.url_get_user)
    # Печатаем ответ
    print("response =", response_get.json())
    # Проверяем статус ответа
    assert response_get.json()['userStatus'] == 0


# Тест изменения пользователя
@pytest.mark.smoke_API
@pytest.mark.user
def test_put_user():
    # сформируем JSON с нужными полями
    request = generate_json_steps.create_json_user_put()
    # Печатаем запрос
    print(request)
    # Сформмируем URL запроса
    url_put = urls.url_pet_user + "/" + str(request['username'])
    # Печатаем url запроса
    print("url_put =", url_put)
    # Выполним PUT
    response_put = requests.put(url_put, json=request, verify=False)
    # Печатаем результат
    print("result = ", response_put.json())
    # Проверяем ответ
    assert response_put.json()['code'] == 200
    # Передаем запрос
    response_get = requests.get(url_put)
    # Печатаем ответ
    print("response =", response_get.json())
    # Проверяем ответ
    assert response_get.json()['userStatus'] == 0


# Тест удаления пользователя
@pytest.mark.smoke_API
@pytest.mark.user
def test_delete_user():
    # Создадим пользователя для последующего удаления
    post_user(urls.username)
    # Удалим пользователя
    response_delete = request_steps.delete_user(urls.url_delete)
    # Печатаем результат
    print(response_delete)
    # Проверим результат удаления
    assert response_delete.json()['code'] == 200
    # Проверим, что пользователя больше нет
    # Выполним поиск
    response_get = request_steps.request_get(urls.url_delete)
    # Печатаем запрос
    print(response_get)
    # Проверим ответ
    assert response_get.json()['message'] == 'User not found'
