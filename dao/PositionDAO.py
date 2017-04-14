from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Position
from model import base

engine = create_engine('sqlite:///raspBy.db')

base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()

p = Position()