import random
import string


# Создание строки чисел 0-9 заданной длины
def generate_random_number_strings(length):
    result = ""
    for i in range(0, length):
        result += str(random.randint(0, 9))
    return result

# Создание текстовой строки заданной длины
def generate_random_letter_strings(length):
    result = ""
    for i in range(0, length):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return result

# Создание email
def generate_random_email_strings():
    result = ""
    for i in range(0, 8):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    result += "@"
    for i in range(0, 4):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    result += ".com"
    return result

# Создание телефонного номера
def generate_random_phone_number_strings():
    result = "+"
    result += str(random.randint(0, 99))
    for i in range(0, 10):
        result += str(random.randint(0, 9))
    return result

def open_file(file):
    # Открываем файл на чтение
    fp = open(file, 'rb')
    files = {'file': fp}
    return files

def close_file(file):
    # Закроем файл на чтение
    file['file'].close

