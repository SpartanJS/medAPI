#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.1.0
Date : 14 december 2018
Short Description : API Refactor (MVP Pattern)

Description : Tests of the medapp Configuration
Package : -
Functions : -

Content
-------
<TestDevelopmentConfig> : class Test

Current Folder : TEST
/medapp/test/test_config.py

Tasks :
- NOT WORKING

"""

import os
import unittest

from flask import current_app
from flask_testing import TestCase

from medapp.main import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('medapp.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        #self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        #self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == '')


if __name__ == '__main__':
    unittest.main()
