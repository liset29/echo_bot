from sqlalchemy import ForeignKey, func, create_engine
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column, sessionmaker
from typing import Annotated
import datetime

engine = create_engine(
    url='postgresql+psycopg2://postgres:liset29@localhost:5432/mydb',
    echo=False
)
Base = declarative_base()
intpk = Annotated[int, mapped_column(primary_key=True)]

session = sessionmaker(engine)


class Users(Base):
    __tablename__ = 'users'

    chat_id: Mapped[intpk]
    user_name: Mapped[str]
    name: Mapped[str]

    def __repr__(self):
        return f'{self.user_name} {self.name}'


class Message(Base):
    __tablename__ = 'user_message'

    id: Mapped[intpk]
    message: Mapped[str]

    chat_id: Mapped[int] = mapped_column(ForeignKey('users.chat_id'))
    time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


