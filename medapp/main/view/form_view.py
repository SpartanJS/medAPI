#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense Application

Version : v0.1.2
Last updated : 19 december 2019
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

TODO : Reprendre la fonction qui associe les réponses aux OA

"""
import requests as rq

from flask import Flask, render_template, request

from main import app
from main.utils.sf36_form import dict_sf36, sf36_questions
from main.utils.sf36_form_short import sf36_questions_short

@app.route('/')
@app.route('/test')
def test():
    data = "Hello World !"
    return render_template('test.html', data=data)

@app.route('/index')
def index():
    """ TO modify to have a short version (1 page)> sf36_questions_short"""
    return render_template('index_alex.html', data=sf36_questions)

COUNTER = 0
@app.route("/poll", methods = ['POST'])
def poll():
    global COUNTER

    #Fonction qui associe les réponses aux OA MANOMANO
    #MANOMANO
    #TODO : Rajouter une question pour pouvoir ne pas remplir tous les champs example le champ 1, 2 et puis basta
    oa_list = []
    for i in sf36_questions:
        for ans in sf36_questions[i]['answers']:
            if ans not in oa_list:
                oa_list.append(ans)
    dict_oa_sf36 ={}
    for i in range(45,58):
        dict_oa_sf36[i] = oa_list[i-45]
    app.logger.info(dict_oa_sf36)
    #app.logger.info(request.form['fields_1'])
    app.logger.info(request.form['q1'])
    COUNTER = COUNTER + 1
    #Pour les OA (Wow c parti loin dans ma tete)
    #Je retrouve la valeur de offeredanswers, du coup j'associe la clé dans mon
    #dict_oa_sf36  >>> dict_oa_responses[i] = 45 >>> 'oa_id'=45
    dict_oa_responses = {}
    for i in range(1,13):
        for key,value in dict_oa_sf36.items():
            if value == request.form[f'q{i}']:
                dict_oa_responses[f'q{i}']=key
    payload = {
        'r_public_id':f'resp{COUNTER}',
        'questions':[{
                'q_id':f'q{i}',
                's_id':'s1',
                'oa_id':dict_oa_responses[f'q{i}'],
                'a_score':100} for i in range(1,13)]
    }
    app.logger.info(payload)
    """
    r = rq.post('http://127.0.0.1:5000/v1/responses', json=payload)
    app.logger.info(r)
    r_content = r._content.decode("utf-8")
    """
    return render_template('poll.html',data=r_content)
