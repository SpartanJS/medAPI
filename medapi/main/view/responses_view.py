#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Views of the app
Package : flask
Functions : Flask, render_template

Content
-------
/test --- Test Flask Basic
/index --- Test Flask Template

Current Folder : VIEW
/medapi/main/view/responses_view.py

"""

from flask import Flask, render_template

from main import app


@app.route('/test')
def test():
    return "test"

@app.route('/index')
def index():
    data = "Hello World !"
    return render_template('index.html', data=data)
