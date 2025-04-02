from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Login endpoint
    TokenRefreshView,     # Get a new access token
)
from .views import ItemCreateView, ItemUpdateView, ItemListView,ItemDeleteView,ItemDetailView, CategoryCreateView, CategoryListView, CategoryDeleteView, RegisterView, LoginView

urlpatterns = [
    # category urls
    path('category/',CategoryListView.as_view(), name= 'list_category'),
    path('category/create/',CategoryCreateView.as_view(), name= 'create_category'),
    path('category/<int:id>/delete/',CategoryDeleteView.as_view(), name= 'Delete_category'),
    
    
    #  item endpoints
    path('item/', ItemListView.as_view(), name = 'Items' ),
    path('item/create/', ItemCreateView.as_view(), name = 'item_create'),
    path('item/<int:id>/update/', ItemUpdateView.as_view(), name= 'item_update'),
    path('item/<int:id>/detail/', ItemDetailView.as_view(), name = 'item_detail'),
    path('item/<int:id>/delete/', ItemDeleteView.as_view(), name = 'item_delete'),
    
    # user authentication urls
    path('register/',  RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # jwt login urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]
