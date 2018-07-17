from django.urls import path

from .views import (
    product_list,
    product_detail,
)


app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path(
        '<slug:catagory_slug>',
        product_list,
        name='product_list_by_catagory'
    ),
    path('<int:pk>/<slug:slug>', product_detail, name='product_detail'),
]
