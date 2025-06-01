# Dteam-django-practical-test
DTEAM - Django Developer Practical Test
Welcome! This test will help us see how you structure a Django project, work with various tools,
and handle common tasks in web development. Follow the instructions step by step. Good luck!
Requirements:
Follow PEP 8 and other style guidelines, use clear and concise commit messages and docstrings where
needed, structure your project for readability and maintainability, optimize database access using
Django's built-in methods, and provide enough details in your README.
Version Control System
Create a public GitHub repository for this practical test, for example: DTEAN- d j ango -
practical-test.
Put the text of this test (all instructions) into READf1E . md .
For each task, create a separate branch (for example, tasks/task-1 , tasks/task-2 , etc.).
When you finish each task, merge that branch back into main but do not delete the original
task branch.
Python Virtual Environment
Use pyenv to manage the Python version. Create a file named . python -ve rs:ton in your repository
to store the exact Python version.
Use Poetry to manage and store project dependencies. This will create a pyp roj ect . toml file.
Update your README . md with clear instructions on how to set up and use pyenv and Poetry for this project.

Tasks

Task 1: Django Fundamentals
Create a New Django Project
Name it something like CVProj ect .
Use the Python version set up in

Task 2 and the latest stable Django release.
Use SQLite as your database for now.
Create an App and Model
Create a Django app (for example, main ).
Define a CV model with fields like firstname , lastname , ski11s , projects , bio , and contacts .
Organize the data in a way that feels efficient and logical.
Load Initial Data with Fixtures
Create a fixture that contains at least one sample CV instance.
Include instructions in READ8E . md on how to load the fixture.
List Page View and Template
Implement a view for the main page (e.g., / ) to display a list of CV entries.
Use any CSS library to style them nicely.
o	Ensure the data is retrieved from the database efficiently.
Detail Page View
Implement a detail view (e.g., /cv/ <id>/ ) to show all data for a single CV.
Style it nicely and ensure efficient data retrieval. ó. Tests
Add basic tests for the list and detail views.
Update READNE . md with instructions on how to run these tests.

Task 2: PDF Generation Basics
Choose and install any HTML-to-PDF generating library or tool.
Add a 'Download PDF’ button on the CV detail page that allows users to download the CV as a
PDF.

Task 3: REST API Fundamentals
.  Install Django REST Framework (DRF).
Create CRUD endpoints for the CV model (create, retrieve, update, delete).
Add tests to verify that each CRUD action works correctly.

Task 4: Middleware & Request Logging
Create a Request Log Model
You can put this in the existing app or a new app (e.g., aud1t ).
Include fields such as timestamp , HTTP method , path , and  optionally other details like
query string, remote IP, or logged-in user.
Implement Logging Middleware
Write a custom Django middleware class that intercepts each incoming request. Create
a Request Log record in the database with the relevant request data. Keep it efficient.
Recent Requests Page
Create a view (e.g., / 1ogs/ ) showing the 10 most recent logged requests, sorted by
timestamp descending.
Include a template that loops through these entries and displays their timestamp, method, and path.
Test Logging
Ensure your tests verify the logging functionality.

Task 5: Template Context Processors
Create sett:ings context
Create a context processor that injects your entire Django settings into all templates.
Settings Page
Create a view (e.g., /settings/ ) that displays DEBUG and other settings values made available
by the context processor.

Task 6: Docker Basics
Use Docker Compose to containerize your project.
Switch the database from SQLite to PostgreSQL in Docker Compose.
Store all necessary environment variables (database credentials, etc.) in a . env file.

Task 7: Celery Basics
Install and configure Celery, using Redis or RabbitMQ as the broker.
Add a Celery worker to your Docker Compose configuration.
On the CV detail page, add an email input field and a ’Send PDF to Email' button to trigger a Celery
task that emails the PDF.

Task 8: OpenAl Basics
.  On the CV detail page, add a ’Translate’ button and a language selector.
Include these languages: Cornish, Manx, Breton, lnuktitut, Kalaallisut, Romani, Occitan, Ladino,
Northern Sami, Upper Sorbian, Kashubian, Zazaki, Chuvash, Livonian, Tsakonian, Saramaccan, Bislama,
Hook this up to an OpenAl translation API or any other translation mechanism you prefer. The idea is
to translate the CV content into the selected language.
Task 9: Deployment
Deploy this project to DigitalOcean or any other VPS. (If you do not have a DigitalOcean account,
you can use this referral link to create account with $200 on balance: https://m.do.co/c/9Ó7939ea e74)
That's it!
Complete each task thoroughly, commit your work following the branch-and-merge structure, and make
sure your README . md clearly explains how to install, run, and test everything. We look forward to
reviewing your submission!
Thank you!


Preparation
#Install Poetry (macOC)
    #poetry install
#Activate virtual env
    poetry env activate

Task 1

1.1 Add django prodject
django-admin startproject CVProject .

1.2 Add app main
python3 manage.py startapp main
Add CVProject/settings.py info about main in INSTALLED_APPS
Add model
Make migrations
python3 manage.py makemigrations
python3 manage.py migrate

1.3 Add folder Fixtures and json file inside folder
#Load fixture in sqlite
python3 manage.py loaddata main/fixtures/example_cv.json

1.4
python3 manage.py runserver

1.6
python3 manage.py test

Task2
pip install xhtml2pdf

Task3
pip install djangorestframework
python3 manage.py test api

