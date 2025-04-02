from django.shortcuts import render
from .models import Category, Inventory_item
from .serializers import CategorySerializer, InventoryItemSerializer, CustomUserSerializer
from rest_framework import generics, permissions, status
# from django.contrib. auth import authenticate
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken

# user authentication views
# registration view

# inventory item views






# first we need to create categories to be associated to the items
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

# creating the create api view with the logic of perfom create method to see turn the availability to falso if the quantity is == 0
class ItemCreateView(generics.CreateAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    
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
    
# retrieve an single item from the database
class ItemDetailView(generics.RetrieveAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
    lookup_field = 'id'

    
# delete an item
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
