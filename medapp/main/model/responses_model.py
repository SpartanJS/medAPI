#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : implement the responses model (SGBDR)
Package : -
Functions : -
Functions_intern : db

Content
-------
<ResponsesTable> - psql table

Current Folder : MODEL
/medapp/main/model/responses_model.py

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
    r_admin = db.Column(db.String)
