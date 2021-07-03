from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart, name='cart'),
	path('add-cart/<int:product_id>/', views.add_cart, name='add-cart'),
	path('remove-cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
	path('remove-cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]