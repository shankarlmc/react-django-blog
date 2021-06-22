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
2. Create Serializers & Permissions for post model
3. Set Token based authentication system
    - Currently there are no tokens which might be surprising. After all we have existing
    users. However the tokens are only generated after there is an API call for a user to
    log in. We have not done that yet so there are no tokens. We will shortly,

4. Endpoints

    - We also need to create endpoints so users can log in and log out. We could create a
    dedicated users app for this purpose and then add our own urls, views, and serializers.
    However user authentication is an area where we really do not want to make a
    mistake. And since almost all APIs require this functionality, it makes sense that there
    are several excellent and tested third-party packages we can use it instead.
    Notably we will use **django-rest-auth** in combination with **django-allauth** to simplify
    things.
    First we will add log in, log out, and password reset API endpoints. So install **Django-Rest-Auth** by using pip command:
        ```
        pip install django-rest-auth
        ```
        For UserRegistration we use **django-allauth**
        ```
        pip install django-allauth
        ```
        After all of the configuration there is a new end point for user registration:
        *http://127.0.0.1:8000/api/v1/rest-auth/registration*

5. Create Serializer for User model

6. Create Schema and Docs View

7. Create React app for frontend
    ```
    npx create-react-app frontend
    ```


