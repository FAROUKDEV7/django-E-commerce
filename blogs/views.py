from django.shortcuts import render
from .models import Blog
from .form import CommentForm
# Create your views here.


def blog_list(request):
    blog=Blog.objects.all()
    context={
        'blog':blog ,
    }
    return render(request,'blogs/blog_list.html',context)




def blog_detail(request,slug):
    blog=Blog.objects.get(slug=slug)
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid:
            my_form=form.save(commit=False)
            my_form.user=request.user
            my_form.save()
    else:
        form=CommentForm()

    context={
        'blog':blog ,
        'form':form,

        
    }
    return render(request,'blogs/blog_detail.html',context)