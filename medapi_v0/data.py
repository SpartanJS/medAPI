#! usr/bin/flaskenv python3
# -*-coding:Utf-8 -*
import json

"""
    Declaration of the "model" DTO : Data Transfert object

    Json Model
    patient DTO
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


issues : Dans les examples v2 (pas besoin de déclarer "ID" et "HREF" ca le fait automatiquement)

"""

alex = {
        #'id': 'resp1',
        #'href': '/api/responses/r1',
        'questions': [
                        {
                        'q_id':'q1',
                        'text': 'Vous sentiez vous enthousiaste?',
                        'answer_id':'a1',
                        'answer_text':'Tout le temps',
                        'answer_score': 100
                        },
                        {
                        'q_id':'q2',
                        'text': 'Avez vous beaucoup d energie ?',
                        'answer_id': 'a2',
                        'answer_text': 'Tout le temps',
                        'answer_score': 100
                        },
                        {
                        'q_id':'q3',
                        'text': 'Avez vous l impression d etre epuise ?',
                        'answer_id': 'a3',
                        'answer_text': 'Jamais',
                        'answer_score': 100
                        }
                    ]
        }

aline = {
        #'id': 'resp2',
        #'href': '/api/responses/r2',
        'questions': [
                        {
                        'q_id':'q10',
                        'text': 'Vous sentiez vous enthousiaste?',
                        'answer_id':'a10',
                        'answer_text':'Jamais',
                        'answer_score': 0
                        },
                        {
                        'q_id':'q20',
                        'text': 'Avez vous beaucoup d energie ?',
                        'answer_id':'a20',
                        'answer_text':'Jamais',
                        'answer_score': 0
                        },
                        {
                        'q_id':'q30',
                        'text': 'Avez vous l impression d etre epuise ?',
                        'answer_id':'a30',
                        'answer_text':'Tout le temps',
                        'answer_score': 0
                        }
                    ]
        }

alice = {
        #'id': 'resp2',
        #'href': '/api/responses/r2',
        'questions': [
                        {
                        'q_id':'qxxx',
                        'text': 'xxx',
                        'answer_id':'axxx',
                        'answer_text':'xxx',
                        'answer_score': 999
                        },
                        {
                        'q_id':'qxxx',
                        'text': 'xxx',
                        'answer_id':'a20',
                        'answer_text':'xxx',
                        'answer_score': 999
                        },
                        {
                        'q_id':'qxxx',
                        'text': 'xxx',
                        'answer_id':'axxx',
                        'answer_text':'xxx',
                        'answer_score': 999
                        }
                    ]
        }
""" Test pour le 'TestButton' """
payload = {"questions": [{"q_id":"q100","answer_id":"a100","answer_score":50},{"q_id":"q200","answer_id":"a200","answer_score":40},{"q_id":"q300","answer_id":"a300","answer_score":60}]}
url = 'http://localhost:5000/apiv1/responses'
#r = requests.post(url,json=payload )
#CF Request documentation
""" Query examples

POST /responses :
curl http://localhost:5000/apiv1/responses -d '{"questions": [{"q_id":"q100","answer_id":"a100","answer_score":50,"text":null},{"q_id":"q200","answer_id":"a200","answer_score":40},{"q_id":"q300","answer_id":"a300","answer_score":60}]}' -X POST -H "Content-Type: application/json"

curl http://localhost:5000/apiv1/responses -d '{"questions":[{"q_id":"q9999","answer_id":"a9999"}]}' -X POST -H "Content-Type: application/json"

PUT /responses/responsesid
curl http://localhost:5000/apiv1/responses/resp3 -d '{"questions":[{"q_id":"UPDATED"}]}' -X PUT -H "Content-Type: application/json"

DELETE /responses/responsesid
curl http://localhost:5000/apiv1/responses/resp3 -X DELETE

POST DB :
curl http://localhost:5000/postdb -d '{"questions": [{"q_id":"q1","answer_id":"a100","answer_score":50},{"q_id":"q2","answer_id":"a200","answer_score":40},{"q_id":"q3","answer_id":"a300","answer_score":60}]}' -X POST -H "Content-Type: application/json"


"""
