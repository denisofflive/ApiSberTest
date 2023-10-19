import requests

# Отправка запроса и получения ответа для метода POST
# url - эндпоинт
# request - JSON
def request_post(url, request):
    request = requests.post(url, json=request, verify=False)
    return request

# Отправка запроса и получения ответа для метода GET
# url - эндпоинт
def request_get(url):
    request = requests.get(url, verify=False)
    return request

# Изменение данных методом PUT
# URL - эндпоинт
def request_put(url, request):
    response = requests.put(url, json=request, verify=False)
    return response

# Удаление пользователя
# URL - эндпоинт
def delete_user(url):
    response = requests.delete(url, verify=False)
    return response
