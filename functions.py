import requests
import config as con
import database

user = database.User()
user_mes = database.Message()


def start(chat_id, first_name, last_name):
    if last_name:
        database.User("users", {"chat_id": chat_id, "first_name": first_name, "last_name": last_name})
    else:
        database.User("users", {"chat_id": chat_id, "first_name": first_name})

    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Привет, напиши что нибудь")


def send_meow_message(chat_id, message):
    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text={message} мяу")


def delete_information(chat_id):
    # user.delete("users_mesg", chat_id)
    user_mes.delete("users_mesg", chat_id)

    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Твои данные удалены")


def my_inf(chat_id):
    information = user.select_all(columns="first_name,last_name,users_mesg.message_user", table_name="users",
                                  params=f"JOIN users_mesg USING(chat_id) WHERE users.chat_id={chat_id} ORDER BY time DESC")[
        0]

    requests.get(
        f"{con.SEND_MESSAGE_URL}{chat_id}&text=Имя: {information[0]}, Фамилия: {information[1]}, Последнее сообщение: {information[2]}")


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
    all_message = user.select_all(table_name="users_mesg", columns="time,message_user",
                                  params=f"where chat_id={chat_id}")
    for i in all_message:
        lst.append(i[0] + ": " + i[1])

    lst = "\n".join(lst)

    requests.get(f"{con.SEND_MESSAGE_URL}{chat_id}&text=Твои сообщения: {lst}")


def add_message(chat_id, time_mes, message):
    database.Message("users_mesg", {"chat_id": chat_id, "time": time_mes, "message_user": message})
