#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.2
Last Updated
Date : 18 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Some basic testing for our API
Package : -
Functions : -

Content
-------
None

Current Folder : MEDAPP
medapi/app.py

Ca permet de tester pas mal de choses qu'on voudrait faire directement dans les classes
Mais on les lance ici, pour eviter les problèmes  d'importation de librairies

"""

from main import app

from main.service.initialization_service import test_initialization_service, test_autoincrement, test_oa
from main.utils.sf36_form import sf36_questions

if __name__=='__main__':
        #test_initialization_service()
        #test_autoincrement()
        test_oa()
