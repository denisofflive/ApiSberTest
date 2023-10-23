

# Функция проверяет утверждение, что ID не пустой
def assert_not_none_id(response):
    assert response.json()['id'] is not None
    print("PASSED")


# Функция проверяет утверждение, что ID запросов равны
def assert_equals_response_ids(first, second):
    print("first ", first.json())
    print("second ", second.json())
    assert first.json()["id"] == second.json()["id"]
    print("PASSED")


# Функия проверяет, что значение 'field' равно 'value'
def assert_equals_response_value(response, field, value):
    print("field ", field)
    print("value ", value)
    print("response ", response)
    print("response json ", response.json())
    if type(response.json()[field]) == '<class "int">':
        assert response.json()[field] == int(value)
    elif type(response.json()[field]) == '<class "str">':
        assert response.json()[field] == value
    print("PASSED")


# Функция проверяет, что страницы не существует
def assert_page_not_found(response):
    assert str(response).__contains__("404")
    print("PASSED")
