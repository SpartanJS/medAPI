#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*w

""" Infos : Medsense API

Version : v0.0.4
Date : 14 december 2018

Description : MVC pattern API

"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app

#Package main
from main import db

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
