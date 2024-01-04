import requests

API_URL = "https://api.telegram.org"

token = "6773930324:AAEDAk5APfsCNxmU0dVW7cgG-lKCHz6vf1Q"

url = f"{API_URL}/bot{token}/setMyCommands"
commands = [
    {"command": "/delete", 'description': 'Удаляет инфу'},
    {"command": "/start", 'description': "Запуск бота"},
    {"command": "/my_inf", 'description': 'Говорит кто ты по жизни'},
    {"command": "/for_danil", 'description': 'Исключительно для Данила'},
    {"command": "/my_message", 'description': 'Все сообщения '}

]
params = {"commands": commands}

response = requests.post(url, json=params)




