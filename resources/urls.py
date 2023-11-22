# Функции генерации URL

main_url = "https://petstore.swagger.io/v2"
main_url_user = "https://petstore.swagger.io/v2/user"

url_pet_post = main_url + "/" + "pet"

def url_user_username(username):
    return main_url_user + "/" + username

def url_pet_get_id(pet_id):
    return url_pet_post + "/" + pet_id

def url_pet_get_findByStatus(status):
    return url_pet_post + "/findByStatus?status=" + status

def url_pet_post_uploadImage(pet_id):
    print("url_1", url_pet_post + "/" + pet_id + "/uploadImage")
    return url_pet_post + "/" + pet_id + "/uploadImage"
