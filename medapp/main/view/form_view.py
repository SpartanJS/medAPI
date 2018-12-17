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

Current Folder : VIEW
medapp/main/view/__init__.py

"""
import requests as rq

from flask import Flask, render_template, request

from main import app

dict_poll = {
    1 : {
            'question' : 'Qui est l auteur?',
            'answers' : ['Alex', 'Aline', 'Alice']
        },
    2 : {
            'question' : 'Qui est l admin ?',
            'answers' : ['Alex', 'Aline', 'Alice']
        }
    }


@app.route('/')
@app.route('/test')
def test():
    data = "Hello World !"
    return render_template('test.html', data=data)

@app.route('/index')
def index():
    return render_template('index.html', data=dict_poll)

@app.route("/poll", methods = ['POST'])
def poll():
    payload = {
        "r_public_id":request.form['field_1'],
        "r_admin":request.form['field_2']
        }
    r = rq.post('http://127.0.0.1:5000/v1/responses', json=payload)
    app.logger.info(r)
    r_content = r._content.decode("utf-8")
    return render_template('poll.html',data=r_content)
