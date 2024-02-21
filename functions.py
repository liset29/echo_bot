import requests
import config as con
from echo_bot.func_db import Control


def start(chat_id, name, last_name, user_name):
    Control.insert_users(chat_id, user_name, name)
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Привет, напиши что нибудь")


def send_meow_message(chat_id, message):
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text={message} мяу")


def delete_information(chat_id):
    Control.delete_information(chat_id)
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Твои данные удалены")


def my_inf(chat_id):
    information = Control.select_information(chat_id)
    requests.get(
        f"{con.SEND_MESSAGE_URL}{chat_id}&text=User_name: {information[0]}\n Имя: {information[1]}\n Количество сообщений: {information[2]}")


def for_danil(chat_id):
    caption = "страшно"
    photo_path = con.PHOTO_BOSS
    url = f'{con.API_URL}/bot{con.TOKEN}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def send_danil(chat_id):
    caption = "босс"
    photo_path = con.PHOTO_NO_BOSS
    url = f'{con.API_URL}/bot{con.TOKEN}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def all_message_user(chat_id):
    lst = []
    resul = Control.select_all_message(chat_id)
    for i in resul:
        lst.append(f'{i[1]}:  {i[0]}')

    lst = "\n".join(lst)
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Твои сообщения:\n {lst}")


def add_message(chat_id, time_mes, message, user_name, name):
    Control.insert_message(chat_id, message)


def send_notification_dupl(chat_id):
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=вы уже писали это сообщение")
