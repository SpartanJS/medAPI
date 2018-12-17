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

Current Folder : MEDAPP
medapp/app.py

"""

from main import app


if __name__ == '__main__':
    app.run(port=5001, debug = True)
