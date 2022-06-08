# content-aggregator-django
## summary
here I tried to fetch a third party api and build a custom command to insert
all the data in my database. Later, I will add schedular to schedule task that I no
longer need to give my command manually, it will do my job automically.

Learning items:
    - how to use custom command in django

## how to run locally

1. create virtual environment
2. install packages from requirements.txt file
3. run, python manage.py makemigrations and python manage.py migrate
3. create a superuser
4. run, python manage.py startjobs (it will work as a custom command)
5. run, python manage.py runserver
DONE