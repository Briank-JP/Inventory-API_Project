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
    - Step 2:
        - Create the Model;
            - Write the User model;
                - we are going to create a custom user model. We shall inherit from django abstractbaseuser, and abstractuser models
            - Write other models including the:
                - Category model that shows the diferent categories of items in the inventory system ie; electronics, machenery, etc.
                - Inventory items that has a one to many relationship with the category model(many items can belong to only one category.)
                
    - Step 3;
        - Create a Serializer file (serializers.py) which will help serialize and deserialize our model instances.In this file we shall use/import our models and use them and aslo import serializers from djangorestframework
        - Next we shall use our serialized data in the views(where we create the logic.)
        - In the views file we shall perfom login, logout and registration on the users. We shall also create CRUD opeations.
            - in the views we shall use generic API views that handle all the logic for CRUD operations.
            - we shall also make use of the perfom_create method provided by drf to help us handle the POST request during the creation of an item. This method automatically creates the item when a user sends in a post request.
    - Step 4:
        - Create a urls.py file in the app directory. This file will contain all endpoints for the api.
        - include the app urls in the project urls by importing include and add it to the path.
        -
    - Step 5 User Authentication
            - Implementing user authentication will include creating serializer for our customuser to serialize our fields
            - We also need to hash the password by overriding the create method and also hiding the password from being returned in the api response by setting the write_only field to true
        - Registration:
            -Here we shall use the post method to get the serialized data from the post request.
            - We also included a permission to allow anyon who isnt registered to be able to access the view.
        -Login:
            -  extract the username and password from the request using the get method
            - we used the .get() because if the key is missing it wil return none instead of raisng an error
            -  check if the user credentials are provided,
            - if the correct credentials are goven, authenitcate the user
            - check the provided credetial and user the log the user in
            
        - Authenticating a user using django simplejwt (Json Web Token)
            -We install django jwt using pip install simple-jwt
            - Follow the steps to create the tokens 
            - No need to create a login view as simple-jwt already works the logic automatically
            - simply include the url endpoints and then protected the view classes with the login permisions so that only authenticated users can access them.

    - Step 6 Deploying
        - Steps taken to deploy a project include:
            1. Prepare the application; 
                - set up your settings.py file. This is a very important file to consider during deployment
                - Ensure the development server is running without errors.You can do this by running tests in your tests.py file and not have any failing
                - set Debug = False
                - Still in the settings.py file, you have to configure/ define allowed hosts
                - collect static files
            2. Choosing your hosting provide. For django we have;
                    -aws, digitalocean, pythonanywhere\
            3. Setup server;
                - isntall python, django and 
                - put all your requirements in the requirements file using pip freeze > requirements.txt
                - virtual environment
                - install dependecies
                - setup DB
            4. upload code to the server
                - Some use git clone
                - some manually via ftp (file transfer protocol)
            5. Handle static and media files
            6. setup domain 
            7. monitor 