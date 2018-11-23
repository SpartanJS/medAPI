#! usr/bin/flaskenv python3
# -*-coding:Utf-8 -*
""" Infos : Medsense API Unittest

Test the API endpoints
packages : nose, request
Nose : Good to test External API/ API on Web !
"""
from nose.tools import assert_true
import requests

def test_request_response():
    """ Send a request to the API server and store the response. """
    response = requests.get('http://localhost:5000/api/v1/responses')
    print(response)
    #Confirm that the request response cycle completed successfuly
    assert_true(response.ok)
    #assert response.status_code == 200
    
#To launch script : nosetest test_api_nose.py (Le truc cool on va chercher l'URL)
