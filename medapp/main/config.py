#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : configuration for Dev,Testing & Prod environment
Package : os
Functions : -

Content
-------
<DevelopmentConfig>
<TestingConfig>
<ProductionConfig>
CONFIGS : dict (configs)

Current Folder : MAIN
medapp/main/config.py

"""


import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ Class with standard constants for all environment """
    SECRET_KEY = os.getenv('SECRET_KEY','my_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    """ Class with Constants for development - Inherit from <Config>"""
    USER = 'alex'
    PASSWORD = 'password'
    HOST = 'localhost'
    DATABASE ='medsense_dev_db'

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """ Class with Constants for testing - Inherit from <Config>"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """ Class with Constants for prod - Inherit from <Config>"""
    DEBUG = False

CONFIGS=dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
