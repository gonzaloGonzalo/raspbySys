#Model class

from dao import Base
from datetime import datetime

dbPosition = Base.db
ma = Base.ma

class Position(dbPosition.Model):
    __tablename__ = 'position'
    id = dbPosition.Column('position_id', dbPosition.Integer, primary_key=True)
    createdOn = dbPosition.Column(dbPosition.DateTime)
    name = dbPosition.Column(dbPosition.String)
    latitude = dbPosition.Column(dbPosition.String)
    longitude = dbPosition.Column(dbPosition.String)

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.createdOn = datetime.utcnow()

    def createTable(self):
        dbPosition.create_all()

class PositionSchema(ma.Schema):
    class Meta:
        fields = ('name','latitude','longitude','createdOn')

        # Smart hyperlinking
        #_links = ma.Hyperlinks({
        #    'self': ma.URLFor('author_detail', id='<id>'),
        #    'collection': ma.URLFor('authors')
        #})

