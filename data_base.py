import sqlite3
import time

con = sqlite3.connect("data_base.db")
cur = con.cursor()



def all_message(chat_id):
    all_mess = []
    result = cur.execute(f"SELECT time,message FROM users_mess WHERE chat_id={chat_id}").fetchall()
    for i in result:
        all_mess.append(i[0] + ": " + i[1])

    return "\n".join(all_mess)


def add_inf(chat_id, surname, message):
    seconds = time.time()
    time_mes = time.ctime(seconds)

    name = "пукич"

    result = cur.execute("SELECT chat_id FROM users").fetchall()
    lst = [str(i) for i in result]

    if f"({chat_id},)" not in lst:
        message = str(message)
        lst.append(chat_id)
        cur.execute(f"INSERT INTO users (chat_id,surname,name) VALUES({chat_id},\"{surname}\",\"{name}\")")
        cur.execute(f"INSERT INTO users_mess (chat_id,time,message) VALUES({chat_id},\"{time_mes}\",\"{message}\")")
    else:
        cur.execute(f"INSERT INTO users_mess (chat_id,time,message) VALUES({chat_id},\"{time_mes}\",\"{message}\")")

    con.commit()


def delete_inf(chat_id):
    cur.execute(f"DELETE FROM users WHERE chat_id={chat_id}")
    cur.execute(f"DELETE FROM users_mess WHERE chat_id={chat_id}")
    con.commit()


def my_inf(chat_id):
    message = cur.execute(
        f"SELECT surname, name, users_mess.message FROM users_mess JOIN users ON users.chat_id = users_mess.chat_id WHERE users.chat_id={chat_id}").fetchall()[
        0]
    return message
