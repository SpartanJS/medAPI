#! usr/bin/flaskenv python3
# -*-coding:Utf-8 -*
""" Infos : Medsense API

version : v0.0.1
description : Flask API Canvas for Medsense API
packages : flask, flask_restplus
tasks : - create a canvas
        - define the endpoint : /api/v1/responses
        - define the endpoint : /api/v1/responses/<responses_id>
        - start a good docstring
Issue : curl answer don't take accent on french words

"""

from flask import Flask
from flask_restplus import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data') #Here, the arg is the field that we want

#MODIFY : initial survey_responses
#We can also name survey_responses : responses
responses_dict = {
    'resp1': {'data': 'Pas du tout'},
    'resp2': {'data': 'Tres peu'},
    'resp3': {'data': 'Pas du tout'}
}

class ResponsesList(Resource):
    """ Resource : ResponsesList

    Gather a collection of "Responses" ressource
    Methods :
    GET -- Return a list of ALL responses
    POST -- Create a response to the survey

    Infos : V0.0.1 - The survey has only 1 question
                     We retrieve only 1 answer

    """
    def get(self):
        """ Instance method to READ all responses """
        return responses_dict
    def post(self):
        """ Instance method to CREATE a new response """
        args = parser.parse_args()
        # The if loop allows us to CREATE a new responses if the responses_dict is null
        if responses_dict.keys():
            responses_id_num = int(max(responses_dict.keys()).lstrip('resp')) + 1
        else:
            responses_id_num = 1
        responses_id = f"resp{responses_id_num}"
        responses_dict[responses_id] = {'data': args['data']}
        return responses_dict[responses_id], 201

class Responses(Resource):
    """ Resource : Responses

    Resource that contains a response (list of answers) of a survey
    Methods :
    GET -- Return a response with all details
    PUT -- Replace a response
    DEL -- Delete a response

    """
    def get(self, responses_id):
        """ Instance method to READ a response """
        return responses_dict[responses_id]
    def put(self, responses_id):
        """ Instance method to UPDATE data of a response """
        args = parser.parse_args()
        responses_new = {'data': args['data']}
        responses_dict[responses_id] = responses_new
        return responses_new, 201
    def delete(self, responses_id):
        """ Instance method to DELETE a response """
        del responses_dict[responses_id]
        return '', 204

## API Resources
## Setting the API Resources routing here
api.add_resource(ResponsesList,'/api/v1/responses')
api.add_resource(Responses,'/api/v1/responses/<responses_id>')


@app.route("/test")
def hello():
    """ Test function for the Flask module """
    return "Hello world!"


if __name__ == "__main__":
    app.run(debug=True)
