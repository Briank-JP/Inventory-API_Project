from rest_framework import serializers
from .models import Category, Inventory_item, CustomUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class InventoryItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Inventory_item
        fields = ['id', 'category', 'name', 'description', 'price', 'quantity', 'available', 'created_at', 'updated_at']
        
        def create(self, validated_data):
             # If the item's quantity is 0, mark it as unavailable
            if validated_data.get('quantity', 0) == 0:
                raise serializers.ValidationError('Quantity must be greater than 0')
            
             # Create and return a new Inventory_item instance with the provided data
            return Inventory_item.objects.create(**validated_data)
        
# user authentication serializer
class CustomUserSerializer(serializers.ModelSerializer):
    # hash the password by making it a write only filed
    # password = serializers.CharField(write_only = True) # this only hides the password from the being returd to the api responses but doesnt hash the password
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            "password": {"write_only":True}
        }
        
        # password hash trial
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.Model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
        
    # override the create method to hash the passsword beofr saving it 
    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password']) #we use the set_password method from  django to hash the password
        user.save()
        return user
    
        
        
#
        