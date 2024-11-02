from django.shortcuts import render,get_object_or_404
from .cart import Cart
from pages.models import Product
from django.http import JsonResponse
import json
from .models import Order

# Import some paypal stuff
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

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





def checkout(request):
    cart=Cart(request)
    totals=cart.cart_total()
    host=request.get_host()
    paypal_dict={
        'business':settings.PAYPAL_RECEIVER_EMAIL,
        'amount':totals,
        'item_name':'order',
        'invoice':str(uuid.uuid4()),
        'notify_url':'https://{}{}'.format(host,reverse("paypal-ipn")),
        'notify_url':'https://{}{}'.format(host,reverse("payment_success")),
        'notify_url':'https://{}{}'.format(host,reverse("payment_failed")),
    }


    # create paypal 
    paypal_form=PayPalPaymentsForm(initial=paypal_dict)

    context={
        'totals':totals,
        'paypal_form':paypal_form,
    }

    return render(request,'cart/checkout.html',context)





def payment_success(request):
    return render(request,'cart/payment_success')




def payment_failed(request):
    return render(request,'cart/payment_failed')