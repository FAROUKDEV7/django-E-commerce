from django.shortcuts import render , redirect
from .models import Product , Product_image
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .forms import SignupForm
# Create your views here.


def index(request):
    products=Product.objects.all()
    context={
        'products':products,
    }
    return render(request,'pages/index.html',context)






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


# registeration

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('login success'))
            return redirect('/')
        else:
            messages.success(request,('login failed'))
            return redirect('/')

    
    else:
        return render(request,'registeration/login.html')







def logout_user(request):
    logout(request)
    messages.success(request,("logout success"))
    return redirect('/')





def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,("signup success"))
            return redirect('/')
        else:
            messages.success(request,("signup failed try again"))
            return redirect('/')
                     
    else:
        form=SignupForm()
        return render(request,'registeration/signup.html',{"form":form})
