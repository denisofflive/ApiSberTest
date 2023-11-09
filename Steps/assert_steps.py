import allure

# Функция проверяет утверждение, что ID не пустой
def assert_not_none_id(response):
    with allure.step("Функия проверяет, что ID не NONE"):
        assert response.json()['id'] is not None
        print("PASSED")


# Функция проверяет утверждение, что ID запросов равны
def assert_equals_response_ids(first, second):
    with allure.step("Функия проверяет утверждение, что ID в запросах равны"):
        print("first ", first.json())
        print("second ", second.json())
        assert first.json()["id"] == second.json()["id"]
        print("PASSED")


# Функия проверяет, что значение 'field' равно 'value'
def assert_equals_response_value(response, field, value):
    with allure.step("Функия проверяет, что значение " + field + " равно " + value):
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
    with allure.step("Функия проверяет, что страницы не существует"):
        assert str(response).__contains__("404")
        print("PASSED")

def assert_status_not_found(response):
    with allure.step("Функия проверяет, что статуса не существует"):
        assert str(response).__contains__("200")
        print("PASSED")
