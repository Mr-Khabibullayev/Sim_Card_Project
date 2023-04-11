from django.urls import path
from product.views import home, create_product, delete_product

urlpatterns = [
    path('',home,name="home"),
    path('create-product/',create_product,name="create-product"),
    path('delete-product/<str:pk>/',delete_product,name="delete-product"),
]
