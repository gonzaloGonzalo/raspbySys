#DAO CRUD operations

from dao import Base
from model.Position import Position

PositionDaoDb = Base.db

#Create position
def createPosition(position):
    PositionDaoDb.session.add(position)
    PositionDaoDb.session.commit()

#Find position by ID
def findPositionById(id):
    return Position.query.filter_by(id=id).first()

#Find all positions
def findAllPosition():
    return Position.query.all()

#Delete position by ID
def deletePositionById(id):
    position = findPositionById(id)
    PositionDaoDb.session.delete(position)
    PositionDaoDb.session.commit()

#Update position by ID
def updatePositionById(id, name, longitude, latitude):
    position = findPositionById(id)
    position.name = name
    position.latitude = latitude
    position.longitude = longitude
    PositionDaoDb.session.commit()





