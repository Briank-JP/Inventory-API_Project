from rest_framework import serializers
from .models import Category, Inventory_item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class InventoryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Inventory_item
        fields = ['id', 'category', 'name', 'description', 'price', 'quantity', 'available', 'created_at', 'updated_at']
        
        def create(self, validated_data):
             # If the item's quantity is 0, mark it as unavailable
            if validated_data.get('quantity', 0) == 0:
                raise serializers.ValidationError('Quantity must be greater than 0')
            
             # Create and return a new Inventory_item instance with the provided data
            return Inventory_item.objects.create(**validated_data)
        