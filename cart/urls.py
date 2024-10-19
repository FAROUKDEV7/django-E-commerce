from django.urls import path
from . import views


urlpatterns = [
    path('cart_summary/',views.cart_summary,name='cart_summary'),
    path('add_cart/',views.add_cart,name="add_cart"),
    path('update_cart/',views.update_cart,name="update_cart"),
    path('delete_cart/',views.delete_cart,name="delete_cart"),
]
