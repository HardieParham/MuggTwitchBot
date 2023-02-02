# Standard Imports
import os

# External Imports
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase

base_dir = os.path.abspath(os.path.dirname(__file__))
db_url = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')

engine = create_engine(db_url, echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = 0
    name = ''


    def __repr__():
        pass







if __name__ == "__main__":
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())