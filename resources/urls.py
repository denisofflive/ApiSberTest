main_url = "https://petstore.swagger.io/v2/"

url_pet_post = main_url + "pet"
url_pet_user = main_url + "user"


def url_pet_get_id(pet_id):
    return main_url + "pet/" + pet_id


def url_pet_findbystatus(status):
    return url_pet_post + "/findByStatus?status=" + status
