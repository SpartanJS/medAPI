#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.1
Date : 17 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Trying to post data to the API

"""

import requests

#On remplit le formulaire .... je redirige vers une adresse de sortie
# @app.route("/sortieduformulaire")

#En sortie du formulaire, je cree un payload ...
payload = {"r_public_id":"alexandre","r_admin":"alexandre"}

r = requests.post('http://127.0.0.1:5000/v1/responses',json=payload)
print (r)
