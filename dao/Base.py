#Base class

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_pyfile('dao.cfg')
db = SQLAlchemy(app)
ma = Marshmallow(app)


