import requests
import config as con
import functions as func

commands = {"/delete_information": func.delete_information,
            "/start": func.start,
            "/my_inf": func.my_inf,
            "/for_danil": func.for_danil,
            "/all_message_user": func.all_message_user}


def setMyCommands():
    url = f"{con.API_URL}/bot{con.TOKEN}/setMyCommands"
    all_commands = [
        {"command": "/delete_information", 'description': 'Удаляет инфу'},
        {"command": "/start", 'description': "Запуск бота"},
        {"command": "/my_inf", 'description': 'Говорит кто ты по жизни'},
        {"command": "/for_danil", 'description': 'Исключительно для Данила'},
        {"command": "/all_message_user", 'description': 'Все сообщения '}

    ]
    params = {"commands": all_commands}

    response = requests.post(url, json=params)
