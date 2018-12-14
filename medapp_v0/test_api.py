#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*
""" Infos : Medsense API Unittest

Test the API endpoints
packages : Flask

"""
from __future__ import print_function

import os
import unittest
import json

import apimed

class PollTestCase(unittest.TestCase):

    #Number of interation of Post Test
    NB_POST = 100

    print("Medsense API Unittest\nVersion : v0.0.1")
    print("*****************")

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownclass(cls):
        pass

    def setUp(self):
        """ Things to do before each test """
        self.app = apimed.app.test_client()
        self.app.testing = True
        self.responses_dict = apimed.responses_dict #Available for each test
        self.bool_multipost = False #Avoid Print(POST) multiple times

    def tearDown(self):
        """ Things to do after each test """
        self.bool_multipost = False
        pass

    def test_afirst(self):
        """ Test the route /test """
        rv = self.app.get('/test')
        self.assertEqual(rv.status_code, 200)
        print('Routing Test : OK')


    """
        data_todumps = {'data':'Beaucoup'}
        rv = self.app.post('/api/v1/responses',
            data=json.dumps(data_todumps),
            content_type='application/json')
        """

    """ Unit tests

    Test executed by alphabetic order

    Methods :
    test_get_responses -- Test : Status_code, Response(Json), Response data fields (1 field actually)
    test_post_responses -- Test : Status_code, Response(Json), Response data fields, Response created
    test_get_responses_responses_id -- Test : Status_code, Response(Json), Response data fields
    test_put_responses_responses_id -- Test : Status_code, Response(Json), Response data fields, Response updated
    test_del_responses_responses_id -- Test : Status_code, Response(Json), Response data fields, Response deleted (?)

    """
    def test_get_responses(self):
        """ Test GET '/api/v1/responses' """
        rv = self.app.get('/api/v1/responses')

        #Status code Test
        self.assertEqual(rv.status_code, 200)
        #Json Response Test
        self.assertEqual(rv.get_json(),self.responses_dict)
        print("GET '/api/v1/responses' : OK")

    def test_get_responses_responses_id(self):
        """ Test GET '/api/v1/responses/<responses_id>' """
        #Test with the first existing key : list(responses_dict.keys())[0]
        responses_id_test = list(self.responses_dict.keys())[0]
        #If ERROR
        #print(responses_id_test)
        rv = self.app.get(f"/api/v1/responses/{responses_id_test}")

        #Status code Test
        self.assertEqual(rv.status_code, 200)
        #Json Response Test
        self.assertEqual(rv.get_json(),self.responses_dict[responses_id_test])
        #Json Response Data Test
        self.assertEqual(rv.get_json()['data'],self.responses_dict[responses_id_test]['data'])
        print("GET ONE '/api/v1/responses/<responses_id>' : OK")

    def test_get_responses_responses_id_each(self):
        """ Test GET EACH '/api/v1/responses/<responses_id>' """
        for key in self.responses_dict.keys():
            rv = self.app.get(f"/api/v1/responses/{key}")

            #Status code Test
            self.assertEqual(rv.status_code, 200)
            #Json Response Test
            self.assertEqual(rv.get_json(),self.responses_dict[key])
            #Json Response Data Test
            self.assertEqual(rv.get_json()['data'],self.responses_dict[key]['data'])
        print("GET ALL '/api/v1/responses/<responses_id>' : OK")

    def test_post_responses(self):
        """ Test POST '/api/v1/responses' """
        data_test = {'data': 'data_value'}
        rv = self.app.post('/api/v1/responses', data=data_test)

        #Status code Test
        self.assertEqual(rv.status_code, 201)
        #Json Response Test
        self.assertEqual(rv.get_json(),data_test)
        #Json Response Data Test
        rv = self.app.get('/api/v1/responses')
        rv_str = json.dumps(rv.get_json())
        data_test_str = json.dumps(data_test)
        self.assertIn(data_test_str, rv_str)
        if self.bool_multipost == False:
            print("POST '/api/v1/responses' : OK")

    def test_post_responses_multiples(self):
        """ Test POST multiple '/api/v1/responses' """
        self.bool_multipost = True
        for i in range(self.NB_POST):
            self.test_post_responses()
        print("POST MULTIPLE '/api/v1/responses' : OK")

    def test_post_responses_first(self):
        """ Test POST First Time '/api/v1/responses' """
        self.responses_dict = {}
        self.test_post_responses()
        print("POST FIRST TIME '/api/v1/responses' : OK")

    def test_put_responses_responses_id(self):
        """ Test PUT '/api/v1/responses/<responses_id>' """
        responses_id_test = list(self.responses_dict.keys())[0]
        data_test = {'data': 'data_value'}
        rv = self.app.put(f"/api/v1/responses/{responses_id_test}",
                            data=data_test)

        #Status code Test
        self.assertEqual(rv.status_code, 201)
        #Json Response Test
        self.assertEqual(rv.get_json(), data_test)
        #Json Response Data Test
        self.assertEqual(rv.get_json()['data'], data_test['data'])
        print("PUT '/api/v1/responses/<responses_id>' : OK")

    def test_del_responses_responses_id(self):
        """ Test DELETE '/api/v1/responses/<responses_id' """
        responses_id_test = list(self.responses_dict.keys())[0]
        rv  = self.app.delete(f"/api/v1/responses/{responses_id_test}")

        #Status code Test
        self.assertEqual(rv.status_code, 204)
        #Json Response Test
        #Change the rv.data 'null' from byte to utf-8
        self.assertEqual(rv.data.decode("utf-8"), '')
        #Json Respons Data Test
        rv = self.app.get('/api/v1/responses')
        self.assertNotIn('',rv.get_json())
        print("DELETE '/api/v1/responses/<responses_id>' : OK")



if __name__ == '__main__':
    unittest.main()
