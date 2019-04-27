from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from app import viewsComments
from app import viewsProduct
from app import viewsUser
from app import viewsOrder

urlpatterns = [
    path('admin', admin.site.urls), 
    path('product', viewsProduct.get_product), 
    path('product/add', viewsProduct.add_product),
    path('product/delete', viewsProduct.delete_product),
]
