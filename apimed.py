#! usr/bin/flaskenv python3
# -*-coding:Utf-8 -*
""" Infos : Medsense API

version : v0.0.2 alpha
date :
description : Flask API "MVP" for Medsense API
Packages : flask, flask_restplus
Tasks : - Create the light DTO & DAO for Medsense API
        - Create a Blank Page with a Button to POST data on API
Endpoints : - GET /apiv1/responses
            - GET /apiv1/responses/<responses_id>
Issues : ?
Steps : 1) Canvas of the Flask/flask_restplus
        2) Define the endpoints GET/GETALL
        3) Define the DAO (Get/create/update/delete) to point the examples (replaced after with DB)
        4) Define the DTO/Model
        5) Define the others endpoints POST/UPDATE/DELETE + Define DAO DTO for Update Delete

Important : Pour afficher "joliment" on utilise "skip_none" = True
Si on souhaite bosser correctement sur le model (Versions ultérieures
on devrait passer "skip_none" = False

------------
version : v0.0.1
description : Flask API Canvas for Medsense API
packages : flask, flask_restplus
tasks : - create a canvas
        - define the endpoint : /api/v1/responses
        - define the endpoint : /api/v1/responses/<responses_id>
        - start a good docstring
Issue : curl answer don't take accent on french words
"""
from collections import OrderedDict
import requests as rq
import json


from flask import Flask, request, render_template
from flask_restplus import Resource, Api, fields, marshal_with, marshal, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix

import data #Contains the data examples : 'data.alex & data.aline'


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='0.0.2', title='Medsense API', description='Medsense collecting patient data API')

#Namespace is apiv1 for all the first version
ns = api.namespace('apiv1',description='Medsense Patient CRUD')

#Permet d'utiliser le kwarg skip_none = True dans marshal_with
null = None

#parser = reqparse.RequestParser()
#parser.add_argument('data') #Here, the arg is the field that we want

#MODIFY : initial survey_responses
#We can also name survey_responses : responses
""" Useful to test directly API Endpoints with a responses_dict - without DAO/DTO """
"""
responses_dict = {
    'resp1': data.alex,
    'resp2': data.aline,
}
"""

""" DTO Object

Formating the Json that we received
Responses DTO Model :
{
    id : string
    href : Url
    questions : [ {
        id : String
        text : String
        answer_id : String
        answer_text : String
        answer_score : Integer
                    }]
}

"""
questions_fields = api.model('Questions', {
    'id': fields.String(attribute='q_id'),
    'text': fields.String,
    'answer_id': fields.String,
    'answer_text': fields.String,
    'answer_score': fields.Integer,
})
responses_fields = api.model('ResponsesDTO',
    {
        'id': fields.String(attribute='responses_id'),
        'href': fields.Url('responses_ep'),
        'questions': fields.List(fields.Nested(questions_fields, skip_none=True)),
    })


class ResponsesDAO(object):
    """ DAO Object : Responses

    Data access object for patient responses

    Methods :
    GET -- Return the object
    CREATE -- Create the object
    UPDATE -- Modify the Object
    DELETE -- Delete the object

    Infos : V 0.0.2
    -- The object that we created is just a concatenation of all responses object
    -- To know the "param" of the object "responses" we need the DTO/model
    -- Usefull to increment the creation of "responses"
    """
    def __init__(self):
        """ Initialisation of the ResponsesDAO """
        self.counter = 0
        self.responses = []

    def get(self,id):
        """ Get a "responses" from the ResponsesDAO(object)

        parameters :
        resp -- an element in responses

        """
        for resp in self.responses:
            if resp['responses_id'] == id:
                return resp
        api.abort(404, f"Response : {id} doesn t exist")

    def create(self,data):
        """ Create a "responses" in the ResponsesDAO(Object) """
        """ Responses endpoint shape  : "resp1","resp2"... """
        resp = data
        self.counter = self.counter + 1
        resp['responses_id'] = f"resp{self.counter}"
        self.responses.append(resp)
        return resp

    def update(self, id, data):
        """ Update a "responses" in ResponsesDAO"""
        resp = self.get(id)
        resp.update(data)
        return resp

    def delete(self,id):
        """ Delete a "responses" in ResponsesDAO"""
        resp = self.get(id)
        self.responses.remove(resp)


DAO = ResponsesDAO()
DAO.create(data.alex)
DAO.create(data.aline)


@ns.route('/responses')
class ResponsesList(Resource):
    """ Resource : ResponsesList

    Gather a collection of "Responses" ressource
    Methods :
    GET -- Return a list of ALL responses
    POST -- Create a response to the survey

    Infos : V0.0.2 - The survey has 3 questions
                    We retrieve 1 answer per question !

    """
    @ns.doc('list_responses')
    @ns.marshal_with(responses_fields, skip_none=True)
    def get(self):
        """ Instance method to READ all responses """
        return DAO.responses

    @ns.doc('create_responses')
    @ns.expect(responses_fields)
    @ns.marshal_with(responses_fields, skip_none=True)
    def post(self):
        """ Instance method to CREATE a new response """
        #args = parser.parse_args() #pas besoin ! on prends un payload
        return DAO.create(api.payload),201 #Du coup il faut mettre en donnée curl un Json


@ns.route('/responses/<responses_id>', endpoint='responses_ep')
@ns.response(404, 'Responses not found')
@ns.param('responses_id', 'The responses id')
class Responses(Resource):
    """ Resource : Responses

    Resource that contains a response (list of answers) of a survey
    Methods :
    GET -- Return a response with all details
    PUT -- Replace a response
    DEL -- Delete a response

    """
    @ns.doc('Get_responses')
    @ns.marshal_with(responses_fields, skip_none=True)
    #Le bug c'est que pour construire l'url il va check "ID" et non"responses_ID"
    # or je lui dit que la route c'est "response_id " >> attribute="responses_id"
    def get(self, responses_id):
        """ Instance method to READ a response """
        return DAO.get(responses_id)

    @ns.doc('update_responses')
    @ns.marshal_with(responses_fields, skip_none=True)
    def put(self, responses_id): #Method qui ne changera pas trop
        """ Instance method to UPDATE data of a response """
        return DAO.update(responses_id, api.payload)

    @ns.doc('delete_responses')
    @ns.response(204,'Delete the response')
    def delete(self, responses_id): #Method qui ne changera pas trop
        """ Instance method to DELETE a response """
        DAO.delete(responses_id)
        return '', 204


## API Resources >>> v0.0.1 (deprecated)
## Setting the API Resources routing here
#api.add_resource(ResponsesList,'/api/v1/responses')
#api.add_resource(Responses,'/api/v1/responses/<responses_id>')


@app.route("/test")
def hello():
    """ Test function for the Flask module """
    text_test = 'Texte secret !'
    return "Hello world!"

#Test du Flask + poll
@app.route("/index")
def index():
    data_index = "Hello World"
    return render_template('index.html', data=data_index)

@app.route("/survey")
def survey():
    """ Test Page with a "Button"

    Description : The button will simulate a sending of patient data

    """

    payload = 'hello world'
    return render_template('survey.html')

@app.route("/result", methods = ['POST'])
def result():
    """
        Result of pressing the "Button" on /survey page

    description : We want the button to POST data on the API
    We want to see the result of the POST request onto this page !
    """
    if request.method == 'POST':
        #rv = rq.get('http://localhost:5000/apiv1/responses/resp1')
        payload = {"questions": [{"q_id":"q100","answer_id":"a100","answer_score":50},{"q_id":"q200","answer_id":"a200","answer_score":40},{"q_id":"q300","answer_id":"a300","answer_score":60}]}
        url = 'http://localhost:5000/apiv1/responses'
        rv = rq.post(url,json=payload )
        rv_content = rv._content.decode("utf-8")
        rv_date = rv.headers['Date']
        app.logger.info(rv) # Lecture dans la console de debug de flask
        return render_template('result.html',data=rv_content, data_2=rv_date),201

if __name__ == "__main__":
    app.run(debug=True)
