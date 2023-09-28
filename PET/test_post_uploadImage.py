import requests

def test_post_pet_id_uploadImage():
    url = "https://petstore.swagger.io/v2/pet/"
    request = {}
    request['id'] = 1
    url_post = url + str(request['id']) + "/uploadImage"
    print("url_post =", url_post)
    fp = open('send.txt', 'rb')
    files = {'file': fp}
    resp = requests.post(url_post, files=files)
    fp.close()
    print(resp.text)

    url_get = url + str(request['id'])
    response_get = requests.get(url_get)
    print("response =", response_get.json())
    assert response_get.json()['id'] == 1
    assert response_get.json()['status'] == "OK"

def test_post_upload():
    url = 'https://petstore.swagger.io/v2/pet/3/uploadImage'
    fp = open('send.txt', 'rb')
    files = {'file': fp}
# передаем созданный словарь аргументу `files`
    resp = requests.post(url, files=files)
    fp.close()
    print(resp.text)

