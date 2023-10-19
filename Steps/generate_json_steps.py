from Steps import support_steps as support_steps

# Создаём JSON для метода POST /pet с обязательными параметрами
def create_json_post_pet_required_params():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = [support_steps.generate_random_letter_string(7)]
    print("request = ", request)
    return request

# Создаём JSON для метода POST /pet с обязательными параметрами
def create_json_post_pet_all_params():
    request = {}
    request['name'] = support_steps.generate_random_letter_string(7)
    request['photoUrls'] = [support_steps.generate_random_letter_string(7)]
    request['category'] = {}
    request['category']['name'] = support_steps.generate_random_letter_string(7)
    request['tags'] = [{}]
    request['tags'] [0] ['name'] = support_steps.generate_random_letter_string(7)
    request['status'] = "available"

    print("request = ", request)
    return request