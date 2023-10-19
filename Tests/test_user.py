import requests
import resources.urls as urls
import Steps.support_steps as support_steps


def test_post_create_user():
    request = {}
    request["id"] = support_steps.generate_random_number_string(7)
    request["username"] = support_steps.generate_random_letter_string(7)
    request["firstName"] = support_steps.generate_random_letter_string(7)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_email_string(1)
    request["password"] = support_steps.generate_random_number_string(7)
    request["phone"] = support_steps.generate_random_number_string(7)
    request["userStatus"] = support_steps.generate_random_number_string(7)
    print(request)

    response_post = requests.post(urls.url_pet_user, json=request, verify=False)
    print("result = ", response_post.json())

    assert response_post.json()['code'] == 200


def test_get_user():
    request = {}
    request["id"] = support_steps.generate_random_number_string(7)
    request["username"] = support_steps.generate_random_letter_string(7)
    request["firstName"] = support_steps.generate_random_letter_string(7)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_email_string(1)
    request["password"] = support_steps.generate_random_number_string(7)
    request["phone"] = support_steps.generate_random_number_string(7)
    request["userStatus"] = support_steps.generate_random_number_string(7)
    print(request)

    response_post = requests.post(urls.url_pet_user, json=request, verify=False)
    print("result = ", response_post.json())

    response_get = requests.get(urls.url_get_user)
    print("response =", response_get.json())

    # assert response_get.json()['userStatus'] == 0


def test_put_user():
    request = {}
    request["id"] = support_steps.generate_random_number_string(7)
    request["username"] = support_steps.generate_random_letter_string(7)
    request["firstName"] = support_steps.generate_random_letter_string(7)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_email_string(1)
    request["password"] = support_steps.generate_random_number_string(7)
    request["phone"] = support_steps.generate_random_number_string(7)
    request["userStatus"] = support_steps.generate_random_number_string(7)

    print(request)
    url_put = urls.url_pet_user + "/" + str(request['username'])
    print("url_put =", url_put)
    response_post = requests.put(url_put, json=request, verify=False)
    print("result = ", response_post.json())

    response_get = requests.get(url_put)
    print("response =", response_get.json())

    assert response_get.json()['userStatus'] == 0


def test_delete_user():
    request = {}
    request["id"] = support_steps.generate_random_number_string(7)
    request["username"] = support_steps.generate_random_letter_string(7)
    request["firstName"] = support_steps.generate_random_letter_string(7)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_email_string(1)
    request["password"] = support_steps.generate_random_number_string(7)
    request["phone"] = support_steps.generate_random_number_string(7)
    request["userStatus"] = support_steps.generate_random_number_string(7)
    print(request)

    response_post = requests.post(urls.url_pet_user, json=request, verify=False)
    print("result = ", response_post.json())

    print("URL_delete", urls.url_delete)

    response_delete = requests.delete(urls.url_delete, verify=False)
    print("response =", response_delete.json())

    response_get = requests.get(urls.url_delete, verify=False)
    print("response =", response_get.json())

    # assert response_get.json()['userStatus'] == 0
