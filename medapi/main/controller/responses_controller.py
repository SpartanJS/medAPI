#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Last updated : 18 december 2018
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
<Initialization> : Initialization QuestionsTable, SurveysTable, SurveysQuestionsTable
<Deletedata> : Delete all data from Questions,Surveys, SurveysQuestionsTable
<DeleteSurveysQuestionsData> : Delete all data from SurveysQuestionsData
<DeleteQuestionsData> : Delete all questions from QuestionsTable
<DeleteOneQuestionData> : Delete one question from QuestionsTable


Current Folder : CONTROLLER
/medapi/main/utils/responses_controller.py

TODO : CREER UN MARSHAL pour la sortie !!
Tasks :
- Create a marshal for output of the db (save_new_responses())
- Implement <Responses>
- Name correctly the DELETE class
- Create 2 types of endpoint
    Initdata > Initialization all data
    Initdata/<tablename> > initilization of a specific table
Create 3 types of endpoint Delete
    Deletedata > Delete all data
    Deletedata/<tablename> > Delete data from a specific table
    Deletedata/<tablename>/<data_id> > Delete a spefici data from a table
Create a delete_service ?

TODO : Function to verify if data are initialized

"""

from flask import request
from flask_restplus import Resource

from main import ns, api
from main.utils.responses_dto import ResponsesDTO
from main.service.responses_service import save_new_responses, get_a_responses, get_all_responses
from main.service.responses_service import delete_all_surveys, delete_all_questions, delete_all_surveysquestions
from main.service.responses_service import delete_a_questions, delete_all_offeredanswers
#DEBUG
from main import app
from main.model.responses_model import test_question
from main.service.initialization_service import test_autoincrement

from main.service.initialization_service import INIT_DICT, questionstable_init, surveystable_init, offeredanswerstable_init


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

        data = {
            'r_public_id': 'resp1',
            'questions':[
                    {
                    'a_score':100,
                    's_id':'s1',
                    'q_id':'q1',
                    'oa_id':45, #Tocheck
                    },
                    {
                    'a_score':100,
                    's_id':'s1',
                    'q_id':'q2',
                    'oa_id':50, #Tocheck
                    },
                    {
                    'a_score':100,
                    's_id':'s1',
                    'q_id':'q3',
                    'oa_id':55, #Tocheck
                    },
                    {
                    'a_score':100,
                    's_id':'s1',
                    'q_id':'q4',
                    'oa_id':56, #Tocheck
                    }
                ]
        }
        app.logger.info(api.payload)
        #return save_new_responses(data)
        return save_new_responses(data)


@ns.route('/initdata')
class InitData(Resource):
    def get(self):
        """ TODO : Function to verify if data are initialized """
        #En attendant, je delete avant d'initiliser
        delete_all_surveysquestions()
        delete_all_questions()
        delete_all_surveys()
        delete_all_offeredanswers()

        questionstable_init()
        surveystable_init()
        offeredanswerstable_init()
        return 'Initialized'

@ns.route('/deletedata')
#@ns.hide
class DeleteData(Resource):
    def delete(self):
        delete_all_surveysquestions()
        delete_all_questions()
        delete_all_surveys()
        delete_all_offeredanswers()
        return '',204

@ns.route('/test')
@ns.hide
class Test(Resource):
    def get(self):
        test_autoincrement()
        return 'Done',200



#################################
##### ENDPOINT TO WORK ON #######
#################################
""" A travailler !!!"""
""" Creation d'une route permettant d'initialiser les différentes tables"""
@ns.route('/initialization/<table_name>')
#@ns.hide
class Init(Resource):
    def get(self,table_name):
        return INIT_DICT[table_name]()


@ns.route('/deletequestionsdata')
#@ns.hide
class DeleteQuestionsData(Resource):
    def delete(self):
        delete_all_questions()
        return '',204

@ns.route('/deletesurveysquestionsdata')
#@ns.hide
class DeleteSurveysQuestionsData(Resource):
    def delete(self):
        delete_all_surveysquestions()
        return '',204


@ns.route('/deletequestionsdata/<q_id>')
#@ns.hide
class DeleteOneQuestionData(Resource):
    def delete(self, q_id):
        delete_a_questions(q_id)
        return '',204
