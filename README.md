# medAPI

## version : v0.0.3 alpha

**Date** : 4 décember 2018

**Description** : Flask API "MVP" for Medsense API

**Packages** : flask, flask_restplus

**Task** :
- [x] Create a "Simple" SGBDR cf paper with 3 tables
- [ ] Create the service that link the model(psql) to psqlDB
- [ ] Connect the API to the SGBDR
- [ ] Update the Push button to POST data on DB

----------------------------------------------------
## version : v0.0.2 alpha

**Date** : 3 december 2018

**Description** : Flask API "MVP" for Medsense API

**Packages** : flask, flask_restplus

**Task**  :
- [x] Create the light DTO & DAO for Medsense API
- [x] Create a Blank Page with a Button to POST data on API

Endpoints :

- GET /apiv1/responses
- GET /apiv1/responses/<responses_id>

Issues : Cf TAIGA

Steps :
1. Canvas of the Flask/flask_restplus
2. Define the endpoints GET/GETALL
3. Define the DAO (Get/create/update/delete) to point the examples (replaced after with DB)
4. Define the DTO/Model
5. Define the others endpoints POST/UPDATE/DELETE + Define DAO DTO for Update Delete

Warning : *Pour afficher "joliment" on utilise "skip_none" = True
Si on souhaite bosser correctement sur le model (Versions ultérieures
on devrait passer "skip_none" = False)*

----------------------------------------------------
## version : v0.0.1

**Description** : Flask API Canvas for Medsense API

**Date** : november 2018

packages : flask, flask_restplus

tasks :
- [x] create a canvas
- [x] define the endpoint : /api/v1/responses
- [x] define the endpoint : /api/v1/responses/<responses_id>
- [x] start a good docstring
Issue : curl answer don't take accent on french words
