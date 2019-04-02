# Feature Request project for ISW employees

### Getting Started

By following the instructions you will be able to run the project in your local environment.
The deployment section contains information on deploying the app on production environment.

### Technologies

* python
* flask
* flask-sqlalchemy
* flask-bootstrap
* flask-wtf
* cryptography (for running ```quiz.py```)

### Database

* sqlite

## Project description
* config.py- contains the configuration values for the application like secret_key, database_url etc.
* forms.py- defines wtforms used in the application.
* models.py- contains models for the application.
* quiz.py- file used by me in the debug quiz part
* feature_req_service.py- contains two methods for querying and updating the database
* feature_req.py- contains the app, the routing informations, initializes the db and 
  holds the methods to run the app
* static folder contains the site.css static file
* templates folder holds the view files 

At the root url a user is shown a form where he can put feature request. The form is validated on server side on submission. If the validation fails user is presented with the form again with appropriate error messages. If the validation succeeds the feature request is queried for client id and priority value. Here is the business logic for inserting a new feature request.
* If there doesn’t exist any feature request with same priority for the client the feature request is added.
* Otherwise, all the existing feature requests having same or greater priority compared to the newly requested feature are updated with incremented priority. Incrementation value is 1. All the values are updated and the new feature request is inserted into the db.
* After that the user is redirected to done page where success messages flashed for newly added feature request and name, and priority of updated feature requests if there is any.

### Validation Logic
* All the fields are required
* Title can’t be more than 250 characters long
* Date should be given in MM/dd/yyyy format, past  date is not allowed.
* Description field can’t be more that 1000 characters long


```
At the database layer added an extra column is added in the feature_request table named 'created' which keep tracks of which feature was added when.
```

## Deployment

## To run the app

* pip install pipenv (if not already installed)
* git clone this repository
* pipenv install
* pipenv run python feature_req.py
* create a sqlite db named isw.db in your project root directory.
  * use command ```sqlite3 isw.db```, install sqlite3 if necessary

## Testing

Not provided.

