#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Service to connect responses_model to postgresql
Package : -
Functions : -

Content
-------
save_new_responses(data) : method to link to psql DB
get_a_responses(r_public_id)
get_all_responses()
delete...()

Current Folder : SERVICE
/medapi/main/view/responses_service.py

TODO : ADD a public_id (uuid.uuid4)
TODO : responses_object ? On ne renvoit pas le dict reçu ?
TODO : Create a different page for the others services
"""

from main import db
from main.model.responses_model import ResponsesTable, SurveysTable, QuestionsTable, SurveysQuestionsTable
from main.model.responses_model import OfferedAnswersTable, AnswersTable, SurveysQuestionsAnswersTable
#DEBUG
from main import app

def save_new_responses(data):
    """ Example
    data = {
        'r_public_id': 'resp1',
        'questions':[
                {
                'a_score':100,
                's_id':'s1',
                'q_id':'q1',
                'oa_id':45, #Tocheck
                }
            ]
    }
    """
    new_responses = ResponsesTable(
        r_public_id=data['r_public_id']
    )
    app.logger.info(data['questions'][10])
    new_answers_list = []
    for ans in data['questions']:
        new_answers = AnswersTable(
            a_score=ans['a_score'],
            s_id=ans['s_id'],
            q_id=ans['q_id'],
            oa_id=ans['oa_id'],
            r_table=new_responses
        )
    new_answers_list.append(new_answers_list)

    app.logger.info(data)
    app.logger.info(f"r_public_id {data['r_public_id']}")

    db.session.add(new_responses)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully registered'
    }
    return response_object, 201
    """
    resp = ResponsesTable.query.filter_by(r_public_id=data['r_public_id']).first
    if not resp:
        new_responses = ResponsesTable(
            r_public_id=data['r_public_id'],
            r_admin=data['r_admin']
        )

        db.session.add(new_responses)
        db.session.commit()
        # WARNING response object !!
        response_object = {
            'status': 'success',
            'message': 'Successfully registered'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Response already exists. Please try again'
        }
        return response_object, 400
    """
def get_a_responses(r_public_id):
    return ResponsesTable.query.filter_by(r_public_id=r_public_id).first()

def get_all_responses():
    return ResponsesTable.query.all()



def delete_all_questions():
    QuestionsTable.query.delete()
    db.session.commit()
    return '', app.logger.info('QuestionsTable ALL data : deleted')

def delete_a_questions(q_id):
    #To modify
    QuestionsTable.query.filter_by(q_id=q_id).delete()
    db.session.commit()
    return '', app.logger.info(f"QuestionsTable {q_id} : deleted")

def delete_all_surveys():
    SurveysTable.query.delete()
    db.session.commit()
    return '', app.logger.info('SurveysTable ALL data : deleted')

def delete_all_offeredanswers():
    OfferedAnswersTable.query.delete()
    db.session.commit()
    return '', app.logger.info('OfferedAnswersTable ALL data : deleted')

#Test
def delete_all_surveysquestions():
    db.session.query(SurveysQuestionsTable).delete()
    db.session.commit()
    return '', app.logger.info('SurveysQuestionsTable ALL data : deleted')
