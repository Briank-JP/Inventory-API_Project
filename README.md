# Inventory-API_Project
Brief
- Inventory management API is a capstone project that is designed to help store managers track their store inventory items, manage them : 
        - Add item
        - Update item information, and iteml lists
        - Read all items
        - Delete Items from the inventory.
- This project is built in steps process 
- Steps:
    - Step 1:
        - Create the development server;
            - create a virtual environment(python -m venv myenv)
            - Activate the virtual environment(myenv\scripts\activate.bat)
            - Install django in the environment (pip install django)
            - Start a django project (django-admin startproject project_name)
            - Install Django restframework (pip install djangorestframework)
            - Then change the directory(cd)into the django project directory and start a django app(python manage.py startapp app_name.)
            - Install the app and restframe work in the installed apps(settings.py --> INSTALLED APPS:)
    Step 2:
        - Create the Model;
            - Write the User model;
                - we are going to create a custom user model. We shall inherit from django abstractbaseuser, and abstractuser models
            - Write other models including the:
                - Category model that shows the diferent categories of items in the inventory system ie; electronics, machenery, etc.
                - Inventory items that has a one to many relationship with the category model(many items can belong to only one category.)
                
    Step 3;
        - Create a Serializer file (serializers.py) which will help serialize and deserialize our model instances.In this file we shall use/import our models and use them and aslo import serializers from djangorestframework
        - Next we shall use our serialized data in the views(where we create the logic.)
        - In the views file we shall perfom login, logout and registration on the users. We shall also create CRUD opeations.
    Step 4:
        - Create a urls.py file in the app directory. This file will contain all endpoints for the api.
        - include the app urls in the project urls by importing include and add it to the path.