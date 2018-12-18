#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.2
Create Date : 18 december 2018
Last Modified : 18 december 2018
Short Description : API Refactor (MVP Pattern)

Description : initialisation of some table
Package : -
Functions : -
Functions_intern : db, QuestionsTable, OfferedAnswersTable, SurveysTable, sf36_form

Content
-------
init <SurveysTable>
init <QuestionsTable>
init <OfferedAnswersTable>

Current Folder : utils
/medapp/main/utils/table_initialization.py

"""

from main import db

from main.model.responses_model import QuestionsTable, OfferedAnswersTable, SurveysTable
from main.utils.sf36_form import sf36_questions

questions_sf36 = []
"""
for i in sf36_questions:
    questions = QuestionsTable(
        q_id=i,
        q_text=sf36_questions[i]['questions']
        )
    questions_sf36.append(questions)
"""
questions = QuestionsTable(
    q_id="1",
    q_text="Yo"
    )
questions_sf36.append(questions)

if __name__ == '__main__':
    print(questions_sf36)
