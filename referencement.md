# Referencement

## version : v0.0.1

### Architecture:

 /medapp

   |--- init.py

   |--- manage.py

   |--- requirements.txt

   |--- /test

          |--- responses_tests.py

          |--- responses_tests_nose.py

   |--- /main

          |--- init.py

          |--- config.py > Config db dev,test, prod

          |--- /controller

                   |--- init.py

                   |--- responses_controller.py

          |--- /model  

                   |--- init.py

                   |--- responses_model.py    

          |--- /service

                   |--- init.py

                   |--- responses_service.py

          |--- /utils

                   |--- responses_DTO.py
                   

----------------------------------------

### responses_model.py

**Table attribute:**
- a_ : answers
- oa_: offered answers
- q_ : questions
- r_ : responses
- s_ : surveys
- p_ : patients

**TableClassName:** ResponsesTable

**TableName:** responsestable

**TableRelationship:** r_table


----------------------------------------

### responses_controller.py

**Responses endpoints:**
- /responses
- /responses/<responses_id>

----------------------------------------

### responses_service.py

**Responses services:**
- save_new_responses()
- get_a_responses()
- get_all_responses()


----------------------------------------

###responses_DTO.py

**Responses DTO model:**
- responses_fields('ResponsesFields')

**Responses DTO attribute:**
- a_ : answers
- oa_: offered answers
- q_ : questions
- r_ : responses
- s_ : surveys
- p_ : patients
