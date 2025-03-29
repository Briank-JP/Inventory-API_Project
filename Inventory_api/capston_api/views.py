from django.shortcuts import render
from .models import Category, Inventory_item
from .serializers import CategorySerializer, InventoryItemSerializer
from rest_framework import generics
# Create your views here.
# first we need to create categories to be associated to the items
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
    
# delete an item
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Inventory_item.objects.all()
    serializer_class = InventoryItemSerializer
