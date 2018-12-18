# Classical errors v 0.0.1

#1 Not migrating the database after modification responses_model.py

#2 Autoincrement don t work if we don t have the sequence Table in psql

#3 Model : Don t forget in backref, the first occurence
>>  **backref**=db.backref('a2_table_br', lazy=True))

#4 model : Don t forget to re-read correctly the name of the TABLE

#5 Model : Care of type of x_id(Normal > db.String / Autoincrement > db.Integer)
