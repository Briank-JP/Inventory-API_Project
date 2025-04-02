from .models import Category, Inventory_item
from .serializers import CategorySerializer, InventoryItemSerializer, CustomUserSerializer
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
# import jwt, datetime
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication


# user registration
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allows anyone to register
    def post(self, request):
        serializer = CustomUserSerializer(data = request.data) #use the data from the post request 
        serializer.is_valid(raise_exception = True) #inase the data that is put isnot true/right it will raise an exception error
        serializer.save() #save the serializer
        return Response(serializer.data) #return the serialize and the user data we want

# using simplejwt
#simple jwt already works on  the login view logic so no need to override it
class LoginView(TokenObtainPairView):
    pass

# first we need to create categories to be associated to the items
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [AllowAny]
   
    permission_classes = [permissions.AllowAny]
    
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'id'

# creating the item views
# api view with the logic of perfom create method to see turn the availability to falso if the quantity is == 0
class ItemCreateView(generics.CreateAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    # methode to check availability and quantity
    def perform_create(self,serializer):
        # to make sure an item is not available if the quantiy is == 0
        if serializer.validated_data.get('quantity',0) == 0:
            serializer.validated_data['available'] = False
            
        serializer.save()

# the update view 
class ItemUpdateView(generics.UpdateAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'id'

    
    # methode to check availability and quantity during a put/patch request
    def perform_create(self,serializer):
        # to make sure an item is not available if the quantiy is == 0
        if serializer.validated_data.get('quantity',0) == 0:
            serializer.validated_data['availability'] = False
            
        serializer.save()
        
class ItemListView(generics.ListAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.AllowAny]
    
# retrieve an single item from the database
class ItemDetailView(generics.RetrieveAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    
# delete an item
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
