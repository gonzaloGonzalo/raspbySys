from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, unique=True)
    created_on = Column(VARCHAR, unique=True)
    latitude = Column(VARCHAR, unique=True)
    longitude = Column(VARCHAR, unique=True)