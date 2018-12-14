#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Marshal data to transfer between class
Package : flask_restplus
Functions : fields

Content
-------
<ResponsesDTO> : DTO Object

Current Folder : DTO
/medapp/main/utils/responses_DTO.py

TODO : Description of the responses_fields attributes
TODO : Description of INPUT / OUTPUT different
Todo : Namespace (uselss ?)

"""

from flask_restplus import Namespace, fields

from main import api

class ResponsesDTO:
    #api = api.namespace('v1', description='Medsense API v1')
    responses_fields = api.model('ResponsesFields', {
        'r_id':fields.String,
        'r_public_id': fields.String,
        'r_admin': fields.String,
        'r_status': fields.String(default='Active')

    })
