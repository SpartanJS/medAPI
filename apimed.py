#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*
""" Infos : Medsense API

## version : v0.0.3 gamma

**Date** : 4 décember 2018
**Description** : Flask API "MVP" for Medsense API
**Packages** : flask, flask_restpluos
**Task** :
- [x] Create a "Simple" SGBDR cf paper with 3 tables
- [x] Create the service that link the model(psql) to psqlDB
- [X] Connect the API to the SGBDR
- [X] Update the Push button to POST data on DB

"""
from collections import OrderedDict
import requests as rq
import json
import uuid
import datetime


from flask import Flask, request, render_template
from flask_restplus import Resource, Api, fields, marshal_with, marshal, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix


import data #Contains the data examples : 'data.alex & data.aline'
from models import db
from models import QuestionsTable
from models import AnswersTable
from models import ResponsesTable

USER = 'alex'
PASSWORD = 'password'
HOST = 'localhost'
DATABASE ='medsense_db'

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

api = Api(app, version='0.0.2', title='Medsense API', description='Medsense collecting patient data API')
#Namespace is apiv1 for all the first version
ns = api.namespace('apiv1',description='Medsense Patient CRUD')

db.init_app(app) #SQLAlchemy object linked to my application

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
############################################################################
##########   Service (Mini controller) access to the DB             ########
############################################################################
# Normally we have to put in a other file/folder with "models.py"
#TODO : Check UUID/ Not useful right now
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


############################################################################
##########                       DTO (cf data.py)                   ########
############################################################################
questions_fields = api.model('Questions', {
    'q_id': fields.String(attribute='q_id'),
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

############################################################################
##########                       DAO                                ########
############################################################################
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


############################################################################
##########      Flask Rest Plus Endpoints                           ########
############################################################################
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
        """ Instance method to CREATE a new response"""
        #data = marshal(data,responses_fields) #Autre façon de présenter le marshal
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


############################################################################
##########                Flask Endpoints                           ########
############################################################################
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
        app.logger.info(rv.__dict__) # Lecture dans la console de debug de flask

        return render_template('result.html',data=rv_content, data_2=rv_date),201

@app.route("/surveydb")
def surveydb():
    """ Test Page with a "Button"

    Description : The button will simulate a sending of patient data

    """
    return render_template('surveydb.html')

@app.route("/postdb", methods = ['POST'])
def postdb():
    #A REFAACTOR
    ###########
    #data = marshal(DAO.create(api.payload),responses_fields) #A utiliser quand j'envoie des données en curl
    #Magouillage pour simuler qu'on récupere la reponse d'un POST (pcq je sais pas comment le recup)

    #A MODIFIER pour des demo du PUSH BUtton"
    payload = {"questions": [
        {"q_id":"q1","answer_id":"a1000","answer_score":50},
        {"q_id":"q2","answer_id":"a2000","answer_score":40},
        {"q_id":"q3","answer_id":"a3000","answer_score":60}
    ]}
    data = marshal(DAO.create(payload),responses_fields)
    """ POST DATA in DB """

    # A UTILISER QUE LA PREMIERE FOIS (PRECREATION)
    #OUBIEN DELETE LA DB AVANT DE SE LANCER
    questions_1 = QuestionsTable(
        q_id='q1',
        q_text='Vous sentiez vous enthousiaste ?'
        )
    questions_2 = QuestionsTable(
        q_id='q2',
        q_text='Avez vous beaucoup d energie ?'
    )
    questions_3 = QuestionsTable(
        q_id='q3',
        q_text='Avez vous l impression d etre epuise ?'
    )

    responses_1 = ResponsesTable(
        r_id=data['id'],
        href=data['href']
    )

    AnswersTable(
        a_id=data['questions'][0]['answer_id'],
        a_score=data['questions'][0]['answer_score'],
        responsestable=responses_1,
        questions_id=data['questions'][0]['q_id']
    )
    AnswersTable(
        a_id=data['questions'][1]['answer_id'],
        a_score=data['questions'][1]['answer_score'],
        responsestable=responses_1,
        questions_id=data['questions'][1]['q_id']
    )
    AnswersTable(
        a_id=data['questions'][2]['answer_id'],
        a_score=data['questions'][2]['answer_score'],
        responsestable=responses_1,
        questions_id=data['questions'][2]['q_id']
    )

    db.session.add(questions_1)
    db.session.add(questions_2)
    db.session.add(questions_3)
    db.session.add(responses_1)
    db.session.commit()

    return render_template('resultdb.html',data=data),201

if __name__ == "__main__":
    app.run(debug=True)
