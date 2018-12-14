#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*w

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : To initiate the DB, and to modify the db model
Packages : flask_script, flask_migrate
Functions : Manager, Migrate, MigrateCommand

Content
-------
test() - Testing the file

Current Folder : MEDAPP
/medapp/manage.py

"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#Package main
from main import db,app
#Understanding : manage.py retrieve responses_model from /model
# responses_model is called in /main/__init__.py
# so when we do "from main import db" : We w ill have it

#TODO : modifier le config_name > creer __init__.py dans /medapp avec le nom

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

#Tests à écrire
"""
/Desktop/medAPI/medapp >>> python manage.py test
"""
@manager.command
def test():
    return 'Hello World'

if __name__ == '__main__':
    manager.run()
