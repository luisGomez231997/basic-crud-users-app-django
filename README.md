# basic-crud-users-app-django
App tecnological stack:

1. Languages: Python, JavaScript.
2. Hyper-Text: Html, Css, Yml.
3. Frameworks: Django, Django Rest, Bootstrap4.
4. Database: PostgreSql or MySql.
5. Deploy: Heroku, Cloudinary.
6. Forja: github.

App Functionality:

1. Login screen, to which any employee can log in with email and password.
2. Once access to the application has been granted, the User Profile Screen of the person who has been authenticated should be displayed.
3. The table of subordinates only appears if the user whose profile is being consulted has subordinates.
4. The name of each minion is a link that causes the page with that person's profile to reload.
5. The name of the boss is linked as long as that person is not superior to the currently logged in user. In other words, users can consult their own profile and that of their subordinates, but not that of their boss or their peers.
6. The green area with the amount of sales has the personal sales of the employee whose profile is being displayed, if that employee is a Sales Executive type, or the recursive sum of the sales of his subordinates, if the employee is of any other type. 

App settings to local startup:

1. dowloand the source code of repository.
2. install python 3.8 and pipenv.
3. install MySQL or PostgreSQL or any Sql Database.
4. Create a database and chargue the initial data, in the csv files. 
5. using shell command go to inside of project folder dir in the same level of manage.py file and execute the command pipenv shell.
6. create a .env file and add the project secret values (database credentials, etc...). 
7. execute command: pipenv install.
8. execute command: python manage.py makemigrations.
9. execute command: python manage.py migrate.
10. execute command: python manage.py collectstatics.
11. execute command: python manage.py runserver.
12. Open the url path displayed in the terminal console.

Note: To advanced python users read the Pipfile and use the command in scripts.

App settings to containers startup:

1. using shell command go to inside of project folder dir in the same level of Dockerfile file and execute the command: docker-compose up.
2. Open the url path displayed in the terminal console.

App Live Demo:
1. Link:  
