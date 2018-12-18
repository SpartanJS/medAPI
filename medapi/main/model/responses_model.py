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
- TODO describe a __repr__ of the table
    TODO : Modify the __repr__  : actually data in Table are trunc to 10 caracteres
    they are shown in a "table"
- TODO : Review the table relationship/backref name !
- TODO : Enlever la dbColumn (Test) en trop


"""

from main import db

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def __repr__(self):
        """Define a base way to print models"""
        representation = ""
        representation += "____________________________________________\n"
        for column, value in self.__dict__.items():
            if column != '_sa_instance_state':
                representation += f"| {str(column)[:10:]} "

        representation += "|\n"
        representation += "+--------------------------\n"
        for column, value in self.__dict__.items():
            if column != '_sa_instance_state':
                representation += f"| {str(value)[:10]} "
        representation += "|\n"

        return representation


    '''
    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })
        #TODO a RELIRE
    '''

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
    r_test = db.Column(db.String)

class QuestionsTable(BaseModel,db.Model):
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

    oa_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    oa_text = db.Column(db.String)


class SurveysQuestionsTable(BaseModel, db.Model):
    """Transitory table for linking Surveys & Questions"""
    __tablename__ = 'surveysquestionstable'

    #primary_key ?
    s_id = db.Column(db.String, db.ForeignKey('surveystable.s_id'), primary_key=True, nullable=False)
    s_table = db.relationship('SurveysTable', backref=db.backref('sq1_table_br', lazy=True))
    q_id = db.Column(db.String, db.ForeignKey('questionstable.q_id'), primary_key=True, nullable=False)
    q_table = db.relationship('QuestionsTable', backref=db.backref('sq2_table_br', lazy=True))




class SurveysQuestionsAnswersTable(BaseModel, db.Model):
    """Transitory table for linking Surveys & Questions"""
    __tablename__ = 'surveysquestionsanswerstable'

    s_id = db.Column(db.String, primary_key=True, nullable=False)
    q_id = db.Column(db.String, primary_key=True, nullable=False)
    oa_id = db.Column(db.Integer, db.ForeignKey('offeredanswerstable.oa_id'), primary_key=True, nullable=False)

    db.ForeignKeyConstraint(
        [s_id,q_id],
        [SurveysQuestionsTable.s_id,SurveysQuestionsTable.q_id]
        )

    sq_table = db.relationship('SurveysQuestionsTable',
        primaryjoin="(SurveysQuestionsAnswersTable.s_id == SurveysQuestionsTable.s_id) & (SurveysQuestionsAnswersTable.q_id == SurveysQuestionsTable.q_id)",
        backref=db.backref('sqa1_table_br', lazy=True)
    )
    oa_table = db.relationship('OfferedAnswersTable', backref=db.backref('sqa2_table_br', lazy=True))

class AnswersTable(BaseModel, db.Model):
    """Answers Model for storing different answers data"""
    __tablename__ = 'answerstable'

    a_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_score = db.Column(db.String) #null pour l'instant
    s_id = db.Column(db.String, nullable=False)
    q_id = db.Column(db.String, nullable=False)
    oa_id = db.Column(db.Integer, nullable=False)
    r_id = db.Column(db.Integer, db.ForeignKey('responsestable.r_id'), nullable=False)

    db.ForeignKeyConstraint(
        [s_id, q_id, oa_id],
        [SurveysQuestionsAnswersTable.s_id, SurveysQuestionsAnswersTable.q_id, SurveysQuestionsAnswersTable.oa_id],
        )

    sqa_table = db.relationship('SurveysQuestionsAnswersTable',
        primaryjoin="and_(AnswersTable.s_id == SurveysQuestionsAnswersTable.s_id, AnswersTable.q_id == SurveysQuestionsAnswersTable.q_id, AnswersTable.oa_id == SurveysQuestionsAnswersTable.oa_id)",
        backref=db.backref('a1_table_br', lazy=True)
        )
    r_table = db.relationship('ResponsesTable', backref=db.backref('a3_table_br', lazy=True))


##TEST
def test_question():
    #db.session.add(questions_1)
    #db.session.commit()
    return ''
