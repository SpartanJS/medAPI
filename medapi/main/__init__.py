#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : __init__ file (Core file) Initialisation of Flask & co
Package : Flask, Flask_restplus, SQLAlchemy, werkzeug
Functions : Flask, Api, SQLAlchemy, ProxiFix

Content
-------
app : Flask Object
db : SQLAlchemy Object
api : FlaskRestplus Object
ns : Namespace Object

Parameters
----------
CONFIG_NAME : dev/test/prod


Current Folder : MAIN
/medapi/main/__init__.py

Tasks :
- Implement Bcrypt
- Implements Namespaces
- create_app fonction ? Useful ?
"""

from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix
#from flask_bcrypt import Bcrypt

from main.config import CONFIGS

##############################################
############ CONFIG NAME #####################
##############################################
CONFIG_NAME='dev'

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

app = create_app(CONFIG_NAME)
api = Api(app,
    version='0.0.2',
    title='Medsense API',
    description='Medsense collecting patient data API'
    )
ns = api.namespace('v1', description='Everything about api v1')

"""Import views for the responses"""
from main.view import responses_view

"""Import Responses Model"""
from main.model import responses_model

"""Import API endpoints"""
from main.controller import responses_controller



#api.add_namespace(api_v1)
