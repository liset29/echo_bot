import psycopg2
import config as con


class User:
    def __init__(self, connecting, cursor, table_name=None, data=None):
        self.con = connecting
        self.cur = cursor

        try:
            columns = ', '.join(data.keys())
            values = ', '.join([f"'{value}'" for value in data.values()])

            self.cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values}) ")
        except Exception:
            print("ключ есть")

    def select_all(self, table_name, columns, params=None):
        self.cur.execute(f"SELECT {columns} FROM {table_name} {params}")
        return self.cur.fetchall()

    def delete(self, table_name, chat_id):
        self.cur.execute(f"DELETE FROM {table_name} WHERE chat_id={chat_id}")


def main(chat_id, first_name, last_name, message_user, time_mes):
    if last_name:
        User(connect, cursor, "users", {"chat_id": chat_id, "first_name": first_name, "last_name": last_name})

    else:
        User(connect, cursor, "users", {"chat_id": chat_id, "first_name": first_name})

    User(connect, cursor, "users_mess", {"chat_id": chat_id, "time": time_mes, "message_user": message_user})


connect = psycopg2.connect(
    host=con.HOST,
    user=con.USER,
    password=con.PASSWORD,
    database=con.DATABASE)
connect.autocommit = True
cursor = connect.cursor()
user = User(connect, cursor)
