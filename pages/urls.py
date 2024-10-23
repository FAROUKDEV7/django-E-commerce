from django.urls import path
from . import views,api

app_name='pages'

urlpatterns = [
    path('',views.index,name='index'),
    path('product_list/',views.product_list,name="product_list"),
    path('<str:slug>',views.product_detail,name="product_detail"),
    path('accounts/login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('api/products/',api.Product_List_Api.as_view(),name='product_api'),
    path('api/products/<int:id>',api.Product_Detail_Api.as_view(),name='product_detail_api'),


]
