#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense Application

Version : v0.1.1
Date : 17 december 2018
Short Description : Application avec formulaires connectée avec medAPI

Description : __init__ file
Package : -
Functions : -

Content
-------
None

Current Folder : main
medapp/main/__init__.py

"""

from flask import Flask

app = Flask(__name__)

"""Import views for the responses"""
from main.view import form_view
