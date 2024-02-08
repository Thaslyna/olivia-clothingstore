from django.urls import path
from . import views

app_name = 'cart'

urlpatterns =[
    path('add/<int:product_id>/', views.add_cart, name="add_cart"),
    path('', views.cart_detail, name="cart_detail"),
    path('remove/<int:pro_id>/', views.remove, name="remove"),
    path('delete/<int:pro_id>/', views.deletion, name="delete"),
]