from django.urls import path
from . import views

app_name='pages'

urlpatterns = [
    path('',views.index,name='index'),
    path('product_list/',views.product_list,name="product_list"),
    path('<str:slug>',views.product_detail,name="product_detail"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup,name="signup"),

]
