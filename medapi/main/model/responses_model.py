#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.2
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : implement the responses model (SGBDR)
Package : -
Functions : -
Functions_intern : db

Content
-------
<ResponsesTable> - psql table
<QuestionsTable>
<SurveysTable>
<OfferedAnswersTable>
<SurveysQuestionsTable>
<SurveysQuestionsAnswersTable>
<AnswersTable>

Current Folder : MODEL
/medapi/main/model/responses_model.py

Tasks:
- Description of the dbColumn attributes

"""

from main import db

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })
        #TODO a RELIRE

    def json(self):
        """Define a base way to jsonify models, dealing with datetime objects"""
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

class ResponsesTable(BaseModel, db.Model):
    """Responses Model for storing responses data"""
    __tablename__ = 'responsestable'

    r_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    r_public_id = db.Column(db.String)
    r_status = db.Column(db.String)

class QuestionsTable(BaseModel, db.Model):
    """Questions Model for storing questions data"""
    __tablename__ = 'questionstable'

    q_id = db.Column(db.String, primary_key=True)
    q_text = db.Column(db.String)

class SurveysTable(BaseModel, db.Model):
    """Surveys Model for storing different surveys data"""
    __tablename__ = 'surveystable'

    s_id = db.Column(db.String, primary_key=True)
    s_desc = db.Column(db.String)

class OfferedAnswersTable(BaseModel, db.Model):
    """Surveys Model for storing different surveys data"""
    __tablename__ = 'offeredanswerstable'

    oa_id = db.Column(db.String, primary_key=True, nullable=False)
    oa_text = db.Column(db.String)

class SurveysQuestionsTable(BaseModel, db.Model):
    """Transitory table for linking Surveys & Questions"""
    __tablename__ = 'surveysquestionstable'

    #primary_key ?
    s_id = db.Column(db.String, db.ForeignKey('surveystable.s_id'), primary_key=True, nullable=False)
    q_id = db.Column(db.String, db.ForeignKey('questionstable.q_id'), primary_key=True, nullable=False)
    s_table = db.relationship('SurveysTable', db.backref('sq_table', lazy=True))
    q_table = db.relationship('QuestionsTable', db.backref('sq1_table', lazy=True))

'''
class SurveysQuestionsAnswersTable(BaseModel, db.Model):
    """Transitory table for linking Surveys & Questions"""
    __tablename__ = 'surveysquestionsanswerstable'

    #primary_key ?
    s_id = db.Column(db.String, db.ForeignKey('surveysquestionstable.s_id'), primary_key=True, nullable=False)
    q_id = db.Column(db.String, db.ForeignKey('surveysquestionstable.q_id'), primary_key=True, nullable=False)
    oa_id = db.Column(db.String, db.ForeignKey('offeredanswerstable.oa_id'), primary_key=True, nullable=False)
    s0_table = db.relationship('SurveysQuestionsTable',db.backref('sqa_table', lazy=True))
    q0_table = db.relationship('SurveysQuestionsTable', db.backref('sqa1_table', lazy=True))
    oa0_table = db.relationship('OfferedAnswersTable', db.backref('sqa2_table', lazy=True))

class AnswersTable(BaseModel, db.Model):
    """Answers Model for storing different answers data"""
    __tablename__ = 'answerstable'

    #primary_key ?
    a_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_score = db.Column(db.String) #null pour l'instant
    s_id = db.Column(db.String, db.ForeignKey('surveysquestionsanswerstable.s_id'), primary_key=True, nullable=False)
    q_id = db.Column(db.String, db.ForeignKey('surveysquestionsanswerstable.q_id'), primary_key=True, nullable=False)
    oa_id = db.Column(db.String, db.ForeignKey('surveysquestionsanswerstable.oa_id'), primary_key=True, nullable=False)
    r_public_id = db.Column(db.String, db.ForeignKey('responsestable.r_id'), nullable=False)
    s1_table = db.relationship('SurveysQuestionsAnswersTable', db.backref('a_table', lazy=True))
    q1_table = db.relationship('SurveysQuestionsAnswersTable', db.backref('a1_table', lazy=True))
    oa1_table = db.relationship('SurveysQuestionsAnswersTable', db.backref('a2_table', lazy=True))
    r1_table = db.relationship('ResponsesTable', db.backref('a3_table', lazy=True))
'''
