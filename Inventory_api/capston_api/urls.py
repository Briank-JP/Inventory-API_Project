from django.contrib import admin
from django.urls import path
from .views import ItemCreateView, ItemUpdateView, ItemListView,ItemDeleteView,ItemDetailView, CategoryCreateView, CategoryListView

urlpatterns = [
    # category urls
    path('category/',CategoryListView.as_view(), name= 'list_category'),
    path('category/create',CategoryCreateView.as_view(), name= 'create_category'),
    #  item endpoints
    path('item/', ItemListView.as_view(), name = 'Items' ),
    path('item/create/', ItemCreateView.as_view(), name = 'item_create'),
    path('item/<int:id>/update', ItemUpdateView.as_view(), name= 'item_update'),
    path('item/<int:id>/detail', ItemDetailView.as_view(), name = 'item_detail'),
    path('item/<int:id>/delete/', ItemDeleteView.as_view(), name = 'item_delete'),
    
    
]
