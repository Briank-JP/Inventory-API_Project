Creating the Inventory API process and explanations(documentation and what is happening in the code.)
- Models:
    - user model:
        - we are going to creat a custom user model that inherits from abstract user and then set roles wic include; Admin- can perfom all crud operations, and regular user - can only view the inventory items.
        - Include the customuser model in the settings.py file to avoid errors during migrations(AUTH_USER_MODEL = "app_name.uc=sermodelname")
    - The category model that categorizes all items into different areas. it has a one to many relationship with the iten inventory mode.
    - Inventory Item model;
         this one stores all attributes of a certain product.

- After settinng the models, makemigrations and migrate.


Serializers:
    - Create a serializer.py file where we shall convert the python data types into json and viseverser.
    - youwill make use of the django restframewors serializers(from restframework imoirt serializers.)
    then point the serial izer to the model