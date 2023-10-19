# Функции генерации URL
from Steps import support_steps

main_url = "https://petstore.swagger.io/v2/"

username = support_steps.generate_random_letter_strings(5)

url_pet_post = main_url + "pet"
url_pet_user = main_url + "user"
url_get_user = url_pet_user + "/" + username
url_delete = url_pet_user + "/" + username


def url_pet_get_id(pet_id):
    return main_url + "pet/" + pet_id


def url_pet_findbystatus(status):
    return url_pet_post + "/findByStatus?status=" + status


def url_pet_post_uploadimage(pet_id):
    print("url_1", url_pet_post + "/" + pet_id + "/uploadImage")
    return url_pet_post + "/" + pet_id + "/uploadImage"
