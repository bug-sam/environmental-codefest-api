from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from api.config import config_by_name
from api.controllers import api


def create_app(config_name):
    # create app
    app = Flask(__name__)

    # config app
    app.config.from_object(config_by_name[config_name])

    # initialize database
    db.init_app(app)

    # add controllers to api
    api.init_app(app)

    return app
