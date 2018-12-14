#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.0.4
Date : 14 december 2018
Description : MVC pattern API

Views of the app

packages : flask
functions : Flask, render_template

Current Folder : VIEW
/medapp/main/view/responses_app.py

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
