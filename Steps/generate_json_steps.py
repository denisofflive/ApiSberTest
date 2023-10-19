from Steps import support_steps as support_steps

# Создаём JSON для метода POST /pet с обязательными параметрами
def create_json_post_pet_required_params():
    request = {}
    request['name'] = support_steps.generate_random_letter_strings(5)
    request['category'] = {}
    request['category']['name'] = support_steps.generate_random_letter_strings(5)
    request['photoUrls'] = [support_steps.generate_random_letter_strings(5)]
    print("request =", request)
    return request

# Создаём JSON для метода POST /pet с обязательными параметрами
def create_json_post_pet_all_params():
    request = {}
    request['id'] = support_steps.generate_random_letter_strings(7)
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
    request = {}
    request['id'] = id
    request['name'] = "sberMan"
    print("request =", request)
    return request

# Создаем JSON для метода PUT /user
def create_json_user_put():
    request = {}
    request['id'] = 1
    request['username'] = "Kitty"
    request['firstname'] = "Cat"
    request['lastname'] = "Sber"
    request['email'] = "denzel@sber.net"
    request['password'] = "sber_mir"
    request['phone'] = "123-45-67"
    request['userstatus'] = "0"
    print("request =", request)
    return request
