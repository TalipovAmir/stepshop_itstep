from django.urls import path

from .views import products, product

urlpatterns = [
    path('', product),
    path('product/', products),

]
