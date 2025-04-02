from django.contrib import admin
from django.urls import path
from .views import ItemCreateView, ItemUpdateView, ItemListView,ItemDeleteView,ItemDetailView, CategoryCreateView, CategoryListView, CategoryDeleteView

urlpatterns = [
    # category urls
    path('category/',CategoryListView.as_view(), name= 'list_category'),
    path('category/create/',CategoryCreateView.as_view(), name= 'create_category'),
    path('category/<int:id>/delete/',CategoryDeleteView.as_view(), name= 'Delete_category'),
    
    
    #  item endpoints
    path('item/', ItemListView.as_view(), name = 'Items' ),
    path('item/create/', ItemCreateView.as_view(), name = 'item_create'),
    path('item/<int:id>/update', ItemUpdateView.as_view(), name= 'item_update'),
    path('item/<int:id>/detail/', ItemDetailView.as_view(), name = 'item_detail'),
    path('item/<int:id>/delete/', ItemDeleteView.as_view(), name = 'item_delete'),
    
    # user authentication urls
    # path('register/',  RegisterAPIView.as_view, name='register'),
    # path('login/', LoginAPIView.as_view, name='login'),
    
    
]
