import pytest
import resources.urls as urls
import Steps.support_steps as support_steps
import Steps.generate_json_steps as generate_json_steps
import Steps.request_steps as requests_steps
import Steps.assert_steps as assert_steps

# Тестирование API для управления пользователями

# Тест создания пользователя
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_post_user():
    # Создаём JSON с обязательными параметрами
    request = generate_json_steps.generate_json_user_random()
    # Отправляем запрос
    response = requests_steps.request_post(urls.main_url_user, request)
    # Анализируем ответ
    assert_steps.assert_response_has_status(response, 200)

# Негативный тест создания пользователя
@pytest.mark.regress_tests
def test_post_user_negative():
    # Создать запрос
    request = generate_json_steps.generate_json_post_null()
    # Отправить запрос
    response = requests_steps.request_post(urls.main_url_user, request)
    # Анализируем ответ
    assert_steps.assert_name_is_equal_value(response, "message", "0")

# Тест вывода информации по пользователю
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_get_user():
    # Создаем пользователя
    request_post = generate_json_steps.generate_json_user_random()
    response_post = requests_steps.request_post(urls.main_url_user, request_post)
    # Отправляем запрос GET
    response_get = requests_steps.request_get(urls.url_user_username(request_post['username']))
    # Анализируем ответ
    assert_steps.assert_equals_response_username(response_get, request_post)
    assert_steps.assert_response_has_status(response_get, 200)

# Негативный тест вывода информации по пользователю
@pytest.mark.regress_tests
def test_get_user_negative():
    # Отправляем запрос GET
    response_get = requests_steps.request_get(urls.url_user_username(support_steps.generate_random_letter_strings(20)))
    # Анализируем ответ
    assert_steps.assert_name_is_equal_value(response_get, "type", "error")
    assert_steps.assert_response_has_status(response_get, 404)

# Тест на обновление пользователя
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_put_user():
    # Создаем пользователя
    request_post = generate_json_steps.generate_json_user_random()
    response_post = requests_steps.request_post(urls.main_url_user, request_post)
    # Создаем JSON с обязательными параметрами
    request_put = generate_json_steps.generate_json_update_pet(response_post.json()['message'])
    # Отправляем запрос
    response_put = requests_steps.request_put(urls.url_user_username(str(request_post['username'])), request_put)
    # Анализируем ответ
    assert_steps.assert_response_has_status(response_put, 200)

# Негативный тест на обновление пользователя
@pytest.mark.regress_tests
def test_put_user_negative():
    # Создаем JSON с обязательными параметрами
    request = generate_json_steps.generate_json_put_negative()
    # Отправляем запрос
    response = requests_steps.request_put(urls.url_user_username(support_steps.generate_random_letter_strings(20)), request)
    # Анализируем ответ
    assert_steps.assert_name_is_equal_value(response, "message", "0")
    assert_steps.assert_status_code_body(response, 200)

# Тест на проверку удаления пользователя
@pytest.mark.smoke_tests
@pytest.mark.regress_tests
def test_delete_user():
    # Создаем пользователя
    request_post = generate_json_steps.generate_json_user_random()
    response_post = requests_steps.request_post(urls.main_url_user, request_post)
    # Удаляем пользователя
    response = requests_steps.request_delete(urls.url_user_username(str(request_post['username'])))
    # Анализируем ответ
    assert_steps.assert_response_has_status(response, 200)

# Негативный тест на проверку удаления пользователя
@pytest.mark.regress_tests
def test_delete_user_negative():
    # Отправляем запрос
    response = requests_steps.request_delete(urls.url_user_username(support_steps.generate_random_letter_strings(20)))
    # Анализируем ответ
    assert_steps.assert_response_has_status(response, 404)

# pytest test_user_api.py::test_del_negative_user - v - s
# pytest -m smoke_regression
# pytest test_post -n3
