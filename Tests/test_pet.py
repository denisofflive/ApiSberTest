import pytest
import requests
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.request_steps as requests_steps
import Steps.assert_steps as assert_steps

# Тестирование API для управления питомцами

# Тест создания питомца
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.parametrize('type',
                         [
                             generate_json_steps.generate_json_pet_required_param(),
                             generate_json_steps.generate_json_pet()
                         ],
                         ids=["required_param", "all_param"]
                         )
def test_post_pet(type):
    # Создаем JSON с обязательными параметрами
    request = type
    # Отправляем запрос
    response_post = requests_steps.request_post(urls.url_pet_post, request)
    print("result=", response_post.json())
    # Проверяем, что вернулся непустой ID созданного питомца
    assert_steps.assert_not_none_id(response_post)
    # Проверяем, что созданного питомца можно получить запросом get
    response_get = requests_steps.request_get(urls.url_pet_get_id(str(response_post.json()['id'])))
    print("result get =", response_get.json())
    # Проверяем, что вернулся именно тот ID питомца, с которым его создавали
    assert_steps.assert_equals_response_ids(response_get, response_post)

# Негативный тест создания питомца (вместо имени передаётся массив)
@pytest.mark.regress_tests
def test_post_pet_negative():
    # Создаем json c для создания питомца
    request = generate_json_steps.generate_json_pet()
    # Заменяем в нем имя категории на невалидное
    request["category"]["name"] = []
    # Отправляем запрос
    response_post = requests_steps.request_post(urls.url_pet_post, request)
    print("result =", response_post.json())
    # Проверяем ответ
    assert_steps.assert_equals_response_values(response_post.json()['message'], "something bad happened")

# Тест получения питомца по ID
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_get():
    # Создаем json для питомца
    request = generate_json_steps.generate_json_pet()
    # Отправляем запрос на создание питомца
    response_post = requests_steps.request_post(urls.url_pet_post, request)
    # Отправляем запрос на получение питомца
    response = requests_steps.request_get(urls.url_pet_get_id(str(response_post.json()['id'])))
    # Смотрим, что в статус ответа 200 и что в ответе получили данные питомца
    print("result =", response.json())
    assert_steps.assert_equals_response_ids(response, response_post)
    assert_steps.assert_equals_response_values(response.json()['status'], 'sold')
    assert_steps.assert_response_has_status(response, 200)

# Негативный тест поиска питомца по ID
@pytest.mark.regress_tests
def test_get_pet_id_negative():
    # Отправляем запрос
    response_get = requests_steps.request_get(urls.url_pet_get_id(support_steps.generate_random_number_strings(6)))
    print("result =", response_get.json())
    # Убеждаемся, что питомец не найден
    assert_steps.assert_equals_response_values(response_get.json()['message'], "Pet not found")

# Тест изменения данных о питомце запросом POST
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.parametrize('type',
                         [
                             generate_json_steps.generate_json_pet_required_param(),
                             generate_json_steps.generate_json_pet()
                         ],
                         ids=["required_param", "all_param"]
                         )
def test_post_pet_id(type):
    # Создаем питомца
    request_post = generate_json_steps.generate_json_pet()
    response_post = requests_steps.request_post(urls.url_pet_post, request_post)
    # Обновляем питомца
    request_post_pet = type
    response_post_pet = requests_steps.request_post_petID(urls.url_pet_get_id(str(response_post.json()['id'])), request_post_pet)
    # Анализируем ответ
    assert_steps.assert_status_code_body(response_post_pet, 200)

# Негативный тест - нельзя изменить несуществующего питомца
@pytest.mark.regress_tests
def test_post_pet_negative():
    # задаем произвольное имя питомца
    newname = support_steps.generate_random_letter_strings(6)
    # Готовим и выполняем запрос на обновление
    datamy = "name=" + newname + "&status=sold"
    response_post_update = requests_steps.request_post_update(
        urls.url_pet_get_id(support_steps.generate_random_number_strings(6)), datamy)
    print("response_updated =", response_post_update.json())
    # Проверяем, что ответ содержит статус 404
    assert_steps.assert_response_has_status(response_post_update, 404)

# Тест обновления питомца
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_put_pet():
    # Создаем питомца
    request = generate_json_steps.generate_json_pet_required_param()
    response_post = requests_steps.request_post(urls.url_pet_post, request)
    print("result=", response_post.json())
    # Создаем JSON
    request_put = generate_json_steps.generate_json_update_pet(str(response_post.json()["id"]))
    # Отправляем запрос на обновление
    response_put = requests_steps.request_put(urls.url_pet_post, request_put)
    print("result_put=", response_put.json())
    # Отправляем запрос на получение
    response_get = requests_steps.request_get(urls.url_pet_get_id(str(response_post.json()['id'])))
    # Анализируем ответ и убеждаемся, что имя изменено
    assert_steps.assert_equals_response_values(request_put["name"], response_get.json()["name"])
    assert_steps.assert_equals_response_values(response_put.json()["name"], response_get.json()["name"])

# Негативный тест - нельзя обновить несуществующего питомца
@pytest.mark.regress_tests
def test_put_pet_negative():
    # Формируем json
    request_put = generate_json_steps.generate_json_update_pet(support_steps.generate_random_number_strings(9))
    print(request_put)
    # Отправляем запросом на обновление питомца, которого не создавали:
    response_put_pet = requests_steps.request_put(urls.url_pet_post, request_put)
    print("response_put_pet =", response_put_pet.status_code)
    # Проверяем, что ответ содержит статус 200
    assert_steps.assert_response_has_status(response_put_pet, 200)

# Тест поиска питомца по статусу
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
@pytest.mark.parametrize('status',
                         [
                             "sold",
                             "available",
                             "pending"
                         ],
                         ids=["sold", "available", "pending"]
                         )
def test_get_by_status(status):
    # Создаем питомца с нужным статусом (параметр)
    print(status)
    request = generate_json_steps.generate_json_pet()
    # Подменяем статус на нужный нам
    request['status'] = status
    # Отправляем запрос
    response_post = requests_steps.request_post(urls.url_pet_post, request)
    print("result=", response_post.json())
    # Отправляем запрос на получение питомцев со статусом sold
    response = requests_steps.request_get(urls.url_pet_get_findByStatus(status))
    print("result_get=", response.json())
    # Выполняем проверки полученного результата
    assert_steps.assert_response_has_status(response, 200)
    assert_steps.assert_equals_response_values(response.json()[0]['status'], status)
    assert_steps.assert_response_contains_text(response.json(), (response_post.json()['name']))

# Негативный тест поиска питомца по статусу
@pytest.mark.regress_tests
def test_get_by_status_negative():
    # Отправляем запрос
    response = requests_steps.request_get(
        urls.url_pet_get_findByStatus(support_steps.generate_random_letter_strings(6)))
    print("result_get=", response.json())
    # Проверяем, что ответ содержит статус 200 и список питомцев пуст
    assert_steps.assert_response_has_status(response, 200)
    assert_steps.assert_response_contains_text(response.json(), "[]")

# Тест удаления питомца
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_delete():
    # Создаем json для питомца
    request = generate_json_steps.generate_json_pet()
    # Отправляем запрос на создание питомца
    response_post = requests_steps.request_post(urls.url_pet_post, request)
    print("result =", response_post.json())
    # Теперь удаляем питомца, отправляем запрос
    response_delete = requests_steps.request_delete(urls.url_pet_get_id(str(response_post.json()["id"])))
    print("result delete =", response_delete.json())
    # Проверяем, что ответ содержит статус 200
    assert_steps.assert_response_has_status(response_delete, 200)
    # Пробуем получить удаленного питомца
    response_get = requests_steps.request_get(urls.url_pet_get_id(str(response_post.json()["id"])))
    assert_steps.assert_equals_response_values(response_get.json()['message'], 'Pet not found')

# Негативный тест удаления несуществующего питомца
@pytest.mark.regress_tests
def test_delete_negative():
    # Отправляем запрос на удаление несуществующего питомца
    response_delete = requests_steps.request_delete(urls.url_pet_get_id(support_steps.generate_random_number_strings(6)))
    print("result delete =", response_delete)
    # Проверяем, что ответ содержит статус 404
    assert_steps.assert_response_has_status(response_delete, 404)

# Тест загрузки файла для питомца
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_post_pet_uploadImage():
    # Открываем файл
    fp = open('D:\\ApiSberTest\\files\\send.txt', 'rb')
    files = {'file': fp}
    # Формируем запрос
    response = requests.post(urls.url_pet_post_uploadImage('2'), files=files)
    fp.close()
    print(response.text)
    # Проверяем запрос
    response_get = requests.get(urls.url_pet_get_id('1'))
    print("response =", response_get.json())
    # Проверяем ответ
    assert_steps.assert_equals_response_values(1, 1)

# Негативный тест загрузки файла для несуществующего питомца
@pytest.mark.regress_tests
def test_post_pet_uploadImage_negative():
    # Работа с файлом
    fp = open('D:\\ApiSberTest\\files\\send.txt', 'rb')
    files = {'file': fp}
    # Пробуем загрузить файл для несуществующего питомца
    response_post_image = requests_steps.request_post_image(
        urls.url_pet_post_uploadImage(support_steps.generate_random_letter_strings(6)), files)
    # Проверяем, что ответ содержит статус 404
    assert_steps.assert_response_has_status(response_post_image, 404)
    # Закрываем чтение файла
    fp.close()

# pytest test_get.py::test_get -v -s
# pytest -m smoke_regression
