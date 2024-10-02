from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.utils.text import slugify
# Create your models here.


class Product(models.Model):
    PRDname=models.CharField(max_length=200,verbose_name=_('product name'))
    PRDcategory=models.ForeignKey('Category',verbose_name=_('product category'),blank=True, null=True,on_delete=models.CASCADE)
    PRDbrand=models.ForeignKey('settings.Brand',verbose_name=_('product brand'),on_delete=models.CASCADE , blank=True, null=True)
    PRDbase_productimage=models.ImageField(upload_to='products/%y/%m/%d' , verbose_name=_('product image'))
    PRDdescription=models.TextField(max_length=500,verbose_name=_('product description'))
    PRDprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('product price'))
    PRDdiscountprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('product offer'),blank=True, null=True)
    PRDisnew=models.BooleanField(blank=True, null=True,verbose_name=_('is new product'))
    PRDcreated=models.DateTimeField(verbose_name=_('product created'))
    PRDbestsellers=models.BooleanField(default=False,verbose_name=_('best sellesrs'))
    PRDnewarrivals=models.BooleanField(default=False,verbose_name=_('new arrivals'))
    PRDhotsales=models.BooleanField(default=False,verbose_name=_('hot sales'))
    slug=models.SlugField(blank=True, null=True)



    def save(self, *args, **kwargs):
        self.slug=slugify(self.PRDname)
        super(Product, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.PRDname





class Product_image(models.Model):
    IMproduct_name=models.ForeignKey('Product',verbose_name=_('product name'), on_delete=models.CASCADE)
    IMimage_product=models.ImageField(upload_to='product_detail/%y/%m/%d',verbose_name=_('product images'))

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.IMproduct_name)




class Category(models.Model):
    CATname=models.CharField(max_length=200,verbose_name=_('category name'))
    CATparent=models.ForeignKey('self',limit_choices_to={'CATparent__isnull':True},blank=True, null=True,verbose_name=_('parent category'),on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.CATname
    


class Product_Alternative(models.Model):
    ALproduct_name=models.ForeignKey('Product',verbose_name=_('product name'),on_delete=models.CASCADE,related_name='product_name')
    ALproduct_alternative=models.ManyToManyField('Product',verbose_name=_('product alternative'),related_name='product_alternative')


    class Meta:
        verbose_name = 'Product alternative'
        verbose_name_plural = 'Products alternative'

    def __str__(self):
        return str(self.ALproduct_name)



class Product_Accessories(models.Model):
    ACproduct_name=models.ForeignKey('Product',verbose_name=_('product name'),on_delete=models.CASCADE,related_name='products_name')
    ACproduct_accessories=models.ManyToManyField('Product',verbose_name=_('product accessories'),related_name='product_accessories')
    
    class Meta:
        verbose_name = 'Accessory'
        verbose_name_plural = 'Accessories'

    def __str__(self):
        return str(self.ACproduct_name)






    

    
    


