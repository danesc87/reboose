# REBOOSE
This is a tiny project written in Python and Flask to make a small web system to remember books and series.  
>* Backend is a REST service
>* Frontend should be developed


* **Contents**
  * Requirements
  * Deploy
  * URL's

### Requirements
This micro-service needs the following requirements to work:
>* python >= 3
>* Flask
>* Flask-SQLAlchemy
>* Flask-Migrate

### Deploy
To deploy REBOOSE it's necessary to create DB and it's tables before running the application, the following code could
 do that:

#### Migrations
Migrations for **Books** microservice  
```bash
cd books/
```
```bash
flask db init
```
```bash
flask db migrate
```
```bash
flask db upgrade
```

#### Run
```bash
python run.py
```