# Project Steps

1. Setup environment for Backend
    ```
    pyhton -m venv venv
    # activate virtual environment by using: 
    venv\Scripts\activate 
    # install all the required dependencies 
    pip install django
    # start django project
    django-admin startproject backend
    # create posts app
    python manage.py createapp posts
    # create superuser
    python manage.py createsuperuser
    # Create Model for Post & migrate
    # Install The Django Rest Framework
    pip install djangorestframework
    # Add it to the installed_apps

    ```
    
2. Create React app for frontend
    ```
    npx create-react-app frontend
    ```

3. 

