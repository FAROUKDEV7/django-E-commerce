from django.shortcuts import render,get_object_or_404
from .cart import Cart
from pages.models import Product
from django.http import JsonResponse
# Create your views here.

def add_cart(request):
    cart=Cart(request)
    if request.POST.get("action") == "post":
        product_id=int(request.POST.get('product_id'))
        product=get_object_or_404(Product,id=product_id)
        cart.add(product=product)
        cart_quantity=cart.__len__()
        response=JsonResponse({'qty':cart_quantity})
        return response




def update_cart(request):
    pass




def delete_cart(request):
    pass

