#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.2
Create Date : 18 december 2018
Last Modified : 18 december 2018
Short Description : API Refactor (MVP Pattern)

Description : initialisation of some table
C'est dans service : car on interagit avec la DB
Package : -
Functions : -
Functions_intern : db, QuestionsTable, OfferedAnswersTable, SurveysTable, sf36_form

Content
-------
init <SurveysTable>
init <QuestionsTable>
init <OfferedAnswersTable>

Current Folder : service
/medapp/main/service/initialization_service.py

Learning : No need to initiate foreignkey table
TODO : Refactor function with "form" in parameters and not "sf_36" directly
TODO : #Initialized SQLALchemy, put in class
TODO : Verifier qu'on initialize pas des données qu'on a deja entrer (2 X initialization)

CRUCIAL : TODO Initialization_service du SurveysQuestionsAnswersTable !
"""

from main import db

from main.model.responses_model import QuestionsTable, OfferedAnswersTable, SurveysTable, SurveysQuestionsTable
from main.utils.sf36_form import sf36_questions
from main.model.responses_model import SurveysQuestionsAnswersTable
#Test
from main import app
from main.model.responses_model import ResponsesTable


questions_sf36 = []

#Initialized <QuestionsTable> SQLAlchemy object

for i in sf36_questions:

    questions = QuestionsTable(q_id=f"q{i}",q_text=sf36_questions[i]['questions'])
    questions_sf36.append(questions)

#Initialized <SurveysTable> SQLAlchemy object
surveys_sf36 = SurveysTable(s_id="s1",s_desc="SF-36 Form")

#Initialized <SurveysQuestionsTable> SQLAlchemy object
for quest in questions_sf36:
    SurveysQuestionsTable(s_table=surveys_sf36,q_table=quest)

""" List all different offered answers without redundancy"""
#Initialized <OfferedAnswersTable> SQLAlchemy object
oa_list = []
for i in sf36_questions:
    for ans in sf36_questions[i]['answers']:
        if ans not in oa_list:
            oa_list.append(ans)

offeredanswers_sf36 = []
for oans in oa_list:
    offeredanswers = OfferedAnswersTable(oa_text=oans)
    offeredanswers_sf36.append(offeredanswers)

surveysquestionsanswers_sf36 = []
#TODO à la mano(pas de reflexion) MANO MANO MANO
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q1', oa_id=45))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q1', oa_id=46))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q1', oa_id=47))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q1', oa_id=48))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q1', oa_id=49))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q2', oa_id=50))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q2', oa_id=51))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q2', oa_id=52))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q2', oa_id=53))
surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id='q2', oa_id=54))
for i in range(3,13):
    for j in range (55,58):
        surveysquestionsanswers_sf36.append(SurveysQuestionsAnswersTable(s_id='s1',q_id=f"q{i}",oa_id=j))

def questionstable_init():
    for quest in questions_sf36:
        db.session.add(quest)
    db.session.commit()
    return 'Initialized', app.logger.info('QuestionsTable : Initialized')

def surveystable_init():
    db.session.add(surveys_sf36)
    db.session.commit()
    return 'Initialized', app.logger.info('SurveysTable : Initialized')

def offeredanswerstable_init():
    for oans in offeredanswers_sf36:
        db.session.add(oans)
    db.session.commit()
    return 'Initialized', app.logger.info('SurveysTable : Initialized')

def surveysquestionsanswers_init():
    for sqa in surveysquestionsanswers_sf36:
        db.session.add(sqa)
    db.session.commit()
    return 'Initialized', app.logger.info('SurveysTable : Initialized')

#Pas besoin de surveysquestions_initialization(), il s'initialise avec les autres
#Pas besion d'initializer les tables de foreign key !


def test_initialization_service():
    """Test to work on the __repr__ of BaseModel """
    print(questions_sf36.__dict__)
    print(questions_sf36[1].__dict__)

    for i in sf36_questions:
        print(questions_sf36[i])
    return ''

def test_autoincrement():
    """ A test that is going to add a data into the responsestable & autoincrement r_id"""
    resp = ResponsesTable(r_public_id='Alexandre')
    db.session.add(resp)
    db.session.commit()
    return ''

def test_oa():
    """ A test to understand why we can t initialized the data in offeredanswerstable"""
    print(oa_list)
    print(offeredanswers_sf36[10].__dict__)
    print(offeredanswers_sf36[10])

INIT_DICT = dict(
    questionstable=questionstable_init,
    surveystable=surveystable_init,
    offeredanswerstable=offeredanswerstable_init
)
