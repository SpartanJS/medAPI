#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Designing the api endpoints
GET/POST ----------------- /responses
GET/UPDATE/DELETE -------- /responses/<r_public_id>

packages : flask, flask_restplus
functions : request, Resource
functions_intern : api, ns, responsesDTO, save_new_responses(), get_responses()

Content
-------
<ResponsesList> : GET/POST /responses


Current Folder : CONTROLLER
/medapp/main/utils/responses_controller.py

TODO : CREER UN MARSHAL pour la sortie !!
Tasks :
- Create a marshal for output of the db (save_new_responses())
- Implement <Responses>

"""

from flask import request
from flask_restplus import Resource

from main import ns, api
from main.utils.responses_dto import ResponsesDTO
from main.service.responses_service import save_new_responses, get_a_responses, get_all_responses

#DEBUG
from main import app

#api = ResponsesDTO.api
responses_fields = ResponsesDTO.responses_fields

null = None

@ns.route('/responses')
class ResponsesList(Resource):
    """ Resource : ResponsesList

    Gather a collection of "Responses" ressource
    Methods :
    GET -- Return a list of ALL responses
    POST -- Create a responses

    """

    @ns.doc('list_responses')
    @ns.marshal_with(responses_fields, skip_none=False)
    def get(self):
        """Instance method to read all responses"""
        return get_all_responses()

    @ns.doc('create_responses')
    #@ns.expect(responses_fields)
    #Pas de marshal sur la reponse ? sinon on peut pas afficher response_object
    #@ns.marshal_with(responses_fields, skip_none=False)
    def post(self):
        """Instance method do create a new responses"""
        app.logger.info(api.payload)
        return save_new_responses(api.payload)
