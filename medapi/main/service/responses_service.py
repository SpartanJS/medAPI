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

Current Folder : SERVICE
/medapi/main/view/responses_service.py

TODO : ADD a public_id (uuid.uuid4)
TODO : responses_object ? On ne renvoit pas le dict reçu ?
"""

from main import db
from main.model.responses_model import ResponsesTable

#DEBUG
from main import app

def save_new_responses(data):
    new_responses = ResponsesTable(
        r_public_id=data['r_public_id'],
        r_admin=data['r_admin']
    )
    app.logger.info(data)
    app.logger.info(f"r_public_id {data['r_public_id']}")
    app.logger.info(f"r_admin {data['r_admin']}")

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
