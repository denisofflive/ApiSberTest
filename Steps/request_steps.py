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
