from django.urls import path

from .views import *

urlpatterns = [
    path('products/', pro_index, name='product-list'),
    path('products/add', addProduct, name='add-product'),
    path('products/insert', insertProduct, name='insert-product'),
    path('products/edit/<int:pk>', editProduct, name='edit-product'),
    path('products/del/<int:pk>', delProduct, name='delete-product'),
    path('products/bulkdel', bulkDelProduct, name='bulk-delete-pro'),
    
    path('categories/', cat_index, name="category-list"),
    path('categories/add', addCategory, name='add-category'),
    path('categories/insert', insertCategory, name='insert-category'),
    path('categories/edit/<int:pk>', editCategory, name='edit-category'),
    path('categories/del/<int:pk>', delCategory, name='delete-category'),
    path('categories/bulkdel', bulkDelCategory, name='bulk-delete-cat'),
    # Path cannot deal with class, it deals with as_views instead which inherit from the class
]

