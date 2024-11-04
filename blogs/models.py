from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.utils.text import slugify
# Create your models here.


class Blog(models.Model):
    BLimage=models.ImageField(upload_to='blogs/%y/%m/%d',verbose_name=_('blog image'))
    BLdate=models.DateTimeField(verbose_name=_('date'))
    BLtitle=models.CharField(max_length=400,verbose_name=_('title'))
    BLdescription=models.TextField(max_length=600,verbose_name=_('description'))
    BLauthor=models.CharField(max_length=100,verbose_name=_('author'),blank=True, null=True)
    slug=models.SlugField(blank=True, null=True)
     


    def save(self, *args, **kwargs):
       self.slug=slugify(self.BLtitle)
       super(Blog, self).save(*args, **kwargs)



    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


    def __str__(self):
        return self.BLtitle




class Comment(models.Model):
    name=models.CharField(max_length=20,blank=True, null=True,verbose_name=_("Name"))
    phone=models.CharField(max_length=20,blank=True, null=True,verbose_name=_("Phone"))
    email=models.EmailField(max_length=100,blank=True, null=True,verbose_name=_("Email"))
    comment=models.TextField(max_length=1000,blank=True, null=True,verbose_name=_("comment"))


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



    def __str__(self):
        return self.name
    






    
    