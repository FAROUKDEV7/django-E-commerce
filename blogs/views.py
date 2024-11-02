from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog_list(request):
    blog=Blog.objects.all()
    context={
        'blog':blog ,
    }
    return render(request,'blogs/blog_list.html',context)




def blog_detail(request,slug):
    blog=Blog.objects.get(slug=slug)

    context={
        'blog':blog ,
        
    }
    return render(request,'blogs/blog_detail.html',context)