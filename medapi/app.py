#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : medapp launcher >>> python app.py
Package : -
Functions : -

Content
-------
None

Current Folder : MEDAPP
medapi/app.py

"""

from main import app


if __name__ == '__main__':
    app.run(debug = True)
