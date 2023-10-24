from Steps import support_steps as support_steps
import allure

# Создаём JSON для метода POST /pet с обязательными параметрами
def create_json_post_pet_required_params():
    with allure.step("Создаем JSON для метода POST /pet с обязательными параметрами"):
        request = {}
        request['name'] = support_steps.generate_random_letter_strings(6)
        request['category'] = {}
        request['category']['name'] = support_steps.generate_random_letter_strings(6)
        request['photoUrls'] = [support_steps.generate_random_letter_strings(6)]
        print("request =", request)
        return request

# Создаём JSON для метода POST /pet с обязательными параметрами
def create_json_post_pet_all_params():
    with allure.step("Создаем JSON для метода POST /pet со всеми параметрами c генерацией ID"):
        request = {}
        request['id'] = support_steps.generate_random_number_strings(7)
        request['category'] = {}
        request['category']['id'] = support_steps.generate_random_number_strings(7)
        request['category']['name'] = support_steps.generate_random_letter_strings(7)
        request['name'] = support_steps.generate_random_letter_strings(7)
        request['photoUrls'] = [support_steps.generate_random_letter_strings(7)]
        request['tags'] = [{}]
        request['tags'][0]['id'] = support_steps.generate_random_number_strings(7)
        request['tags'][0]['name'] = support_steps.generate_random_letter_strings(7)
        request['status'] = "sold"
        print("request =", request)
        return request

# Создаем JSON для метода POST /pet со всеми параметрами для заданного ID
def create_json_pet_all_param_id(id_num):
    with allure.step("Создаем JSON для метода POST /pet со всеми параметрами для заданного ID"):
        request = {}
        request['id'] = id_num
        request['category'] = {}
        request['category']['id'] = support_steps.generate_random_number_strings(7)
        request['category']['name'] = support_steps.generate_random_letter_strings(7)
        request['name'] = support_steps.generate_random_letter_strings(7)
        request['photoUrls'] = [support_steps.generate_random_letter_strings(7)]
        request['tags'] = [{}]
        request['tags'][0]['id'] = support_steps.generate_random_number_strings(7)
        request['tags'][0]['name'] = support_steps.generate_random_letter_strings(7)
        request['status'] = "sold"
        print("request =", request)
        return request

# Создаем JSON для метода POST /user со всеми параметрами для заданного ID
def create_json_pet_user(username):
    with allure.step("Создаем JSON для метода POST /pet со всеми параметрами для заданного ID"):
        request = {}
        request['id'] = support_steps.generate_random_number_strings(7)
        if username == '':
            request['username'] = support_steps.generate_random_letter_strings(7)
        else:
            request['username'] = username
        request['firstname'] = support_steps.generate_random_letter_strings(7)
        request['lastname'] = support_steps.generate_random_letter_strings(7)
        request['email'] = support_steps.generate_random_email_strings(1)
        request['password'] = support_steps.generate_random_letter_strings(7)
        request['phone'] = support_steps.generate_random_number_strings(7)
        request['userstatus'] = support_steps.generate_random_letter_strings(7)
        print(request)
        return request

# Создаем JSON для метода PUT /pet
def create_json_pet_put(id):
    with allure.step("Создаем JSON для метода PUT /pet"):
        request = {}
        request['id'] = id
        request['name'] = "sberWowKitten"
        print("request =", request)
        return request

# Создаем JSON для метода PUT /user
def create_json_user_put():
    with allure.step("Создаем JSON для метода PUT /user"):
        request = {}
        request['id'] = 1
        request['username'] = "Catty"
        request['firstname'] = "Cat"
        request['lastname'] = "Sber"
        request['email'] = "SberCat@sber.ru"
        request['password'] = "sber_pass"
        request['phone'] = "999-99-99"
        request['userstatus'] = "0"
        print("request =", request)
        return request
