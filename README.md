# Housekeeping Portal
Housekeeping Portal made as part of recruitment task at Udaan.

## Setting Up
 - `conda create -n new-env python=3.6`
 - `source activate new-env`
 - `pip install -r requirements.txt`

## Steps to run
 - `cd Mihir_Kawatra_VIT_16BCE0060`
 - `python manage.py makemigrations`
 - `python manage.py migrate`
 - `python manage.py runserver`


 ## NOTE:

 - The API can be further transformed to handle JSON like input request.
 - Styling can also be improved.
 - SQLite has been used for Database for fast prototyping only. Production ready application would use PostgreSQL.
