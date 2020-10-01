from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    config = configparser.ConfigParser()
    config.read('config.ini')
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    global db
    global ma

    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    db.create_all()

    return app