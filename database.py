import psycopg2
import config as con


class User:
    def __init__(self, table_name=None, data=None):

        connecting = psycopg2.connect(
            host=con.HOST,
            user=con.USER,
            password=con.PASSWORD,
            database=con.DATABASE)
        connecting.autocommit = True
        cursor = connecting.cursor()

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


class Message:
    def __init__(self, table_name=None, data=None):
        connecting = psycopg2.connect(
            host=con.HOST,
            user=con.USER,
            password=con.PASSWORD,
            database=con.DATABASE)
        connecting.autocommit = True
        cursor = connecting.cursor()

        self.con = connecting
        self.cur = cursor
        if table_name:
            columns = ', '.join(data.keys())
            values = ', '.join([f"'{value}'" for value in data.values()])

            self.cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values}) ")

    def delete(self, table_name, chat_id):
        self.cur.execute(f"DELETE FROM {table_name} WHERE chat_id={chat_id}")


user = User()
user_mes = Message()