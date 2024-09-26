from django.shortcuts import render
from .models import Product , Product_image
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request,'pages/index.html')






def product_list(request):
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={
        'product_list':page_obj ,
    }
    return render(request,'pages/product_list.html',context)





def product_detail(request,slug):
    product_detail=Product.objects.get(slug=slug)
    product_image=Product_image.objects.filter(IMproduct_name=product_detail)
    context={
        'product_detail':product_detail,
        'product_image':product_image,

    }
    return render(request,'pages/product_detail.html',context)