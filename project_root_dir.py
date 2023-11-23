import os

# Функция для определения root директории проекта
def project_root_dir():
    return os.path.dirname(os.path.abspath(__file__))
