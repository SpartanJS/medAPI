#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense API

Version : v0.0.4
Date : 14 december 2018
Description : MVC pattern API

app : Creation of the app (Flask) object

"""

from main import create_app

app = create_app('dev')

@app.route("/hello")
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug = True)
