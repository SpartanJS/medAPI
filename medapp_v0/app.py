#!usr/bin/medAPIenv python
# -*-coding:Utf-8 -*
""" Infos : Medsense API

version : v0.0.3 gamma
date : 5 décember 2018
description : Testing the DB functionnalities

"""
import uuid
import datetime
from flask import Flask

from models import db
from models import QuestionsTable
from models import AnswersTable
from models import ResponsesTable

USER = 'alex'
PASSWORD = 'password'
HOST = 'localhost'
DATABASE ='medsense_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alex:password@localhost/my_db'

db.init_app(app) #SQLAlchemy object linked to my application

############################################################################
##########   Service (Mini controller) access to the DB             ########
############################################################################
# Normally we have to put in a other file/folder with "models.py"
#TODO : Check UUID
def save_new_answers(data):
    """ POST/SAVE Data in the postgresql Database """
    answers = AnswersTable.query.filter_by(a_id=data['answer_id']).first()
    if not answers:
        new_answers = AnswersTable(
            a_id=data['answer_id'],
            a_text=data['answer_text'],
            a_score=data['answer_score']
        )
        save_changes(new_answers)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message' :'User already exists. Please log in.'
        }
        return response_object, 409

def get_all_answers():
    """ GET ALL data in the postgresql Database """
    return AnswersTable.query.all()

def get_a_user(a_id):
    """ GET Data by a_id in the postgresql Database """
    return AnswersTable.query.filter_by(a_id=data['a_id']).first()

def save_changes(data):
    """ Function to check and commit the sending of data in the psql db """
    db.session.add(data)
    db.session.commit()


#Examples
alex_noob = {
    'answer_id':'a1',
    'answer_text':'Tout le temps',
    'answer_score':100
}
alex = {
        'r_id': 'resp1',
        'href': '/api/responses/r1',
        'questions': [
                        {
                        'q_id':'q1',
                        'answer_id':'a1',
                        'answer_text':'Tout le temps',
                        'answer_score': 100
                        },
                        {
                        'q_id':'q2',
                        'answer_id': 'a2',
                        'answer_text': 'Tout le temps',
                        'answer_score': 100
                        },
                        {
                        'q_id':'q3',
                        'answer_id': 'a3',
                        'answer_text': 'Jamais',
                        'answer_score': 100
                        }
                    ]
        }

@app.route("/test")
def hello():
    """
    #YourModel(id, lat, lng)
    alex = YourModel(id=101,lat=3.5,lng=4)
    db.session.add(alex)
    db.session.commit()
    """
    return "Hello World"

@app.route("/postdb")
def post_test():
    """ We try with a simple example without function to post data"""
    data = alex
    #todo : Faudrai créeer une boucle avec une liste pour les questionstb
    #>>> question[i]

    #Questions : je peux créer en amont ?
    questions_1 = QuestionsTable(
        q_id=data['questions'][0]['q_id'],
        q_text='Vous sentiez vous enthousiaste ?'
        )
    questions_2 = QuestionsTable(
        q_id=data['questions'][1]['q_id'],
        q_text='Avez vous beaucoup d energie ?'
    )
    questions_3 = QuestionsTable(
        q_id=data['questions'][2]['q_id'],
        q_text='Avez vous l impression d etre epuise ?'
    )
    responses_1 = ResponsesTable(
        r_id=data['r_id'],
        href=data['href']
    )
    AnswersTable(
        a_id=data['questions'][0]['answer_id'],
        a_text=data['questions'][0]['answer_text'],
        a_score=data['questions'][0]['answer_score'],
        responsestable=responses_1,
        questionstable=questions_1
    )
    AnswersTable(
        a_id=data['questions'][1]['answer_id'],
        a_text=data['questions'][1]['answer_text'],
        a_score=data['questions'][1]['answer_score'],
        responsestable=responses_1,
        questionstable=questions_2
    )
    AnswersTable(
        a_id=data['questions'][2]['answer_id'],
        a_text=data['questions'][2]['answer_text'],
        a_score=data['questions'][2]['answer_score'],
        responsestable=responses_1,
        questionstable=questions_3
    )
    db.session.add(questions_1)
    db.session.add(questions_2)
    db.session.add(questions_3)
    db.session.add(responses_1)
    db.session.commit()
    return "Done"

    #SELECT * FROM answerstable, responsestable, questionstable WHERE
    # answerstable.response_id=responsestable.r_id AND
    # answerstable.questions_id=questionstable.q_id

    #return save_new_answers(data=alex)

if __name__=="__main__":
    app.run(debug = True)
