from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String

class Users:
    metadata = MetaData()
    users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40)),
                    Column('age', Integer),
                    Column('password', String),
                    )

    def __init__(self, name, alias):
        self.name = name  # public
        self.__alias = alias  # private