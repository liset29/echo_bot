import requests
import data_base
import config as con
send_message=con.SEND_MESSAGE_URL


def send_hello(chat_id):
    requests.get(f"{send_message}{chat_id}&text=Привет, напиши что нибудь")


def send_meow_message(chat_id, message):
    requests.get(f"{send_message}{chat_id}&text={message} мяу")


def delete_message(chat_id):
    data_base.delete_inf(chat_id)
    requests.get(f"{send_message}{chat_id}&text=Твои данные удалены")


def send_users_inf(chat_id):
    information= data_base.my_inf(chat_id)
    requests.get(f"{send_message}{chat_id}&text=Фамилия: {information[0]}, ИМЯ: {information[1]}, сообщение: {information[2]}")


def send_boss(chat_id):
    caption = "страшно"
    photo_path = r'C:\Users\Тимур\danil.jpg'
    url = f'https://api.telegram.org/bot{con.TOKEN}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def send_danil(chat_id):
    caption = "босс"
    photo_path = r'C:\Users\Тимур\danil2.jpg'
    url = f'https://api.telegram.org/bot{con.TOKEN}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def send_all_message(chat_id):
    all_message = data_base.all_message(chat_id)
    requests.get(f"{send_message}{chat_id}&text=Твои сообщения: {all_message}")
