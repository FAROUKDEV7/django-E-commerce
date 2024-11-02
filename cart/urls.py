from django.urls import path , include
from . import views




urlpatterns = [
    path('payment_success',views.payment_success,name="payment_success"),
    path('payment_failed',views.payment_failed,name="payment_failed"),
    path('cart_summary/',views.cart_summary,name='cart_summary'),
    path('add_cart/',views.add_cart,name="add_cart"),
    path('update_cart/',views.update_cart,name="update_cart"),
    path('delete_cart/',views.delete_cart,name="delete_cart"),
    path('checkout/',views.checkout,name='checkout'),
    path('paypal/', include("paypal.standard.ipn.urls")),
]
