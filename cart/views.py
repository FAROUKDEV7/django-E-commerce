from django.shortcuts import render,get_object_or_404
from .cart import Cart
from pages.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    cart=Cart(request)
    product=cart.get_prods()
    totals=cart.cart_total()
    quantities=cart.get_quants
    context={
        'product':product,
        'totals':totals,
        'quantities':quantities,
    }
    return render(request,'cart/cart_summary.html',context)






def add_cart(request):
    cart=Cart(request)
    if request.POST.get("action") == "post":
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product=get_object_or_404(Product,id=product_id)
        cart.add(product=product , quantity=product_qty)
        cart_quantity=cart.__len__()
        response=JsonResponse({'qty':cart_quantity})
        return response




def update_cart(request):
    cart=Cart(request)
    if request.POST.get("action") == "post":
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response=JsonResponse({'qty':product_qty})
        return response




def delete_cart(request):
    cart=Cart(request)
    if request.POST.get("action") == "post":
        product_id=int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response=JsonResponse({'product_id':product_id})
        return response

