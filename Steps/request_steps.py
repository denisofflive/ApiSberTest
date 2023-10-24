import requests
import allure

# Отправка запроса и получения ответа для метода POST
# url - эндпоинт
# request - JSON
def request_post(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        request = requests.post(url, json=request, verify=False)
        return request

# Отправка запроса и получения ответа для метода GET
# url - эндпоинт
def request_get(url):
    with allure.step("Отправка запросов и получение ответа для метода GET"):
        request = requests.get(url, verify=False)
        return request

# Изменение данных методом PUT
# URL - эндпоинт
def request_put(url, request):
    with allure.step("Изменение данных методом PUT"):
        response = requests.put(url, json=request, verify=False)
        return response

# Удаление пользователя
# URL - эндпоинт
def delete_user(url):
    with allure.step("Удаление пользователя"):
        response = requests.delete(url, verify=False)
        return response
