from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    return render(request,'pages/index.html')






def product_list(request):
    product_list=Product.objects.all()
    context={
        'product_list':product_list ,
    }
    return render(request,'pages/product_list.html',context)