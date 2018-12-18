#! usr/bin/medAPIenv python3
# -*-coding:Utf-8 -*

""" Infos : Medsense Application

Version : v0.1.1
Date : 17 december 2018
Short Description : Application avec formulaires connectée avec medAPI

Description : SF 36 form in a dict
Package : -
Functions : -

Content
-------
None

Current Folder : UTILS
medapp/main/utils/__init__.py

ATTention : modification par rapport au SF36_form.py de medAPP (questions[0])

"""

dict_sf36 = {
    1 : {
            'questions' : 'Qui est l auteur?',
            'answers' : ['Alex', 'Aline', 'Alice']
        },
    2 : {
            'questions' : 'Qui est l admin ?',
            'answers' : ['Alex', 'Aline', 'Alice']
        }
    }


sf36_questions = {
    0: {
        'questions': 'test question ?',
        'answers': [
                    'answers1'
                    ]
        },
    1: {
        'questions': 'En général, diriez-vous que votre santé est :',
        'answers': [
                    'Excellente',
                    'Très bonne',
                    'Bonne',
                    'Satisfaisante',
                    'Mauvaise'
                    ]
        },
    2: {
        'questions': 'Par comparaison avec il y a un an, que diriez-vous sur '\
                     'votre santé aujourd\'hui ?',
        'answers': [
                    'Bien meilleure qu\'il y a un an',
                    'Un peu meilleure qu\'il y a un an',
                    'A peu près comme il y a un an',
                    'Un peu moins bonne qu\'il y a un an',
                    'Pire qu\'il y a un an'
                    ]
        },
    3: {
        'intro': 'Vous pourriez vous livrer aux activiés suivantes le même jour. '\
                 'Est-ce que votre état de santé vous impose des limites dans ces '\
                 'activités ? Si oui, dans quelle mesure ?',
        'questions': 'Activités intenses : courir, soulever des objets lourds, faire du sport.',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    4 :{
        'questions': 'Activités modérées : déplacer une table, passer l\'aspirateur.',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    5 :{
        'questions': 'Soulever et transporter les achats d\'alimentation.',
        #question ripou
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    6 :{
        'questions': 'Monter plusieurs étages à la suite.',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    7 :{
        'questions': 'Monter un seul étage',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    8 :{
        'questions': 'Vous agenouiller, vous accroupir ou vous pencher très bas',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    9 :{
        'questions': 'Marcher plus d\'un kilomètre et demi.',
        #question ripou
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    10 :{
        'questions': 'Marcher plus de 500 mètres',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    11 :{
        'questions': 'Marcher seulement 100 mètres',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },
    12 :{
        'questions': 'Prendre un bain, une douche ou vous habiller',
        'answers': [
                    'Oui, très limité',
                    'Oui, plutôt limité',
                    'Pas limité du tout'
                    ]
    },

}

if __name__ == '__main__':
    for i in sf36_questions:
        print(sf36_questions[i]['questions'])
