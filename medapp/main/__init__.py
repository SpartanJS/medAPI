#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.0.4
Date : 14 december 2018
Description : MVC pattern API

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix
#from flask_bcrypt import Bcrypt

from .config import CONFIGS


db = SQLAlchemy()
#flask_bcrypt = Bcrypt()


def create_app(config_name):
    """ Initialisation of the Flask app & modules """
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(CONFIGS[config_name])
    db.init_app(app)
    #flask_bcrypt.init_app(app)

    return app
