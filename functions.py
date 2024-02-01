import requests
import config as con
from database import user, user_mes


def start(chat_id):
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Привет, напиши что нибудь")


def send_meow_message(chat_id, message):
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text={message} мяу")


def delete_information(chat_id):
    user.delete("users_mess", chat_id)
    user_mes.delete("users", chat_id)

    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Твои данные удалены")


def my_inf(chat_id):
    information = user.select_all(columns="first_name,last_name,users_mess.message_user", table_name="users",
                                  params=f"JOIN users_mess USING(chat_id) WHERE users.chat_id={chat_id} ORDER BY time DESC")[
        0]

    requests.get(
        f"{con.SEND_MESSAGE_URL}{chat_id}&text=Имя: {information[0]}, Фамилия: {information[1]}, Последнее сообщение: {information[2]}")


def for_danil(chat_id):
    caption = "страшно"
    photo_path = r'C:\Users\Тимур\danil.jpg'
    url = f'{con.API_URL}/bot{con.TOKEN}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def send_danil(chat_id):
    caption = "босс"
    photo_path = r'C:\Users\Тимур\danil2.jpg'
    url = f'{con.API_URL}/bot{con.TOKEN}/sendPhoto'
    files = {'photo': open(photo_path, 'rb')}
    params = {'chat_id': chat_id, 'caption': caption}
    response = requests.post(url, params=params, files=files)


def all_message_user(chat_id):
    lst = []
    all_message = user.select_all(table_name="users_mess", columns="time,message_user",
                                  params=f"where chat_id={chat_id}")
    for i in all_message:
        lst.append(i[0] + ": " + i[1])

    lst = "\n".join(lst)

    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Твои сообщения: {lst}")