from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#definie your models class
class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    #definir here __repr__ and json methods for all models

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
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

#TODO : Mettre des constraints sur les modeles

class QuestionsTable(BaseModel, db.Model):
    __tablename__ = 'questionstable'

    q_id = db.Column(db.String(50), primary_key=True)
    q_text = db.Column(db.String(2000))

class AnswersTable(BaseModel, db.Model):
    __tablename__ = 'answerstable'

    a_id = db.Column(db.String(50), primary_key=True)
    a_text = db.Column(db.String(2000))
    a_score = db.Column(db.Integer)
    #public_id = db.Column(db.String(100))

    responses_id =db.Column(db.String(50), db.ForeignKey('responsestable.r_id'), nullable=False)
    responsestable = db.relationship('ResponsesTable', backref=db.backref('answerstb', lazy=True))
    questions_id =db.Column(db.String(50), db.ForeignKey('questionstable.q_id'), nullable=False)
    questionstable = db.relationship('QuestionsTable', backref=db.backref('questionstb', lazy=True))

class ResponsesTable(BaseModel, db.Model):
    __tablename__ = 'responsestable'

    r_id = db.Column(db.String(50), primary_key=True)
    href = db.Column(db.String(200))
