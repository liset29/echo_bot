from model import Base, Users, Message
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, delete
import config as con

# engine = create_engine(
#     url=f'postgresql+psycopg2://postgres:liset29@localhost:5432/mydb',
#     echo=False
# )
engine = create_engine(
    url=f'postgresql+psycopg2://{con.USER}:{con.PASSWORD}@{con.HOST}:{con.PORT_ORM}/{con.DATABASE}',
    echo=False
)

session = sessionmaker(engine)


class Control:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_users(chat_id, user_name, name):
        with session() as sess:
            try:
                user = Users(user_name=user_name, name=name, chat_id=chat_id)
                sess.add(user)
                sess.commit()
            except Exception:
                print('ключ уже есть')

    @staticmethod
    def insert_message(chat_id, message):
        with session() as sess:
            message = Message(message=message, chat_id=chat_id)
            sess.add(message)
            sess.commit()

    @staticmethod
    def select_all_message(chat_id):
        with session() as sess:
            query = select(Message.message, Message.time).where(Message.chat_id == chat_id)
            result = sess.execute(query)
            res = result.all()
            return res

    @staticmethod
    def delete_information(chat_id):
        with session() as sess:
            query = delete(Message).where(Message.chat_id == chat_id)
            sess.execute(query)
            sess.commit()

    @staticmethod
    def select_information(chat_id):
        with session() as sess:
            query_messages = select(Message.message, Message.time).where(Message.chat_id == chat_id)
            result = sess.execute(query_messages)
            counter_message = len(result.all())
            query = select(Users.user_name, Users.name).where(Users.chat_id == chat_id)
            result = list(*sess.execute(query))
            result.append(counter_message)
            return result


# Control.insert_value()

