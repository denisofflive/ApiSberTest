import requests
import allure

# Отправка запросов и получение ответа для метода POST
# URL - эндпоинт
# request - JSON
def request_post(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        response = requests.post(url, json=request, verify=False)
        return response

# Отправка запросов и получение ответа для метода POST для обновления данных
# URL - эндпоинт
# request - JSON
def request_post_update(url, dataup):
    with allure.step("Отправка запросов и получение ответа для метода POST для обновления данных"):
        response = requests.post(url, data=dataup, verify=False)
        return response

# Отправка запросов и получение ответа для метода PUT
# URL - эндпоинт
# request - JSON
def request_put(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        response = requests.put(url, json=request, verify=False)
        return response

# Отправка запросов и получение ответа для метода POST для отправки файла
# URL - эндпоинт
# files - files
def request_post_image(url, files):
    with allure.step("Отправка запросов и получение ответа для метода POST для отправки файлов"):
        response = requests.post(url, files=files, verify=False)
        return response

# Отправка запроса и получение ответа для метода GET
# url - эндпоинт
def request_get(url):
    with allure.step("Отправка запросов и получение ответа для метода GET"):
        response = requests.get(url, verify=False)
        return response

# Отправка запроса и получение ответа для метода DELETE
# URL - эндпоинт
def request_delete(url, verify=False):
    with allure.step("Отправка запросов и получение ответа для метода DEL"):
        response = requests.delete(url, verify=False)
        return response

# Отправка запроса POST /pet/{petID}
# URL - эндпоинт
# request - JSON
def request_post_petID(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        response = requests.delete(url, json=request, verify=False)
        return response
