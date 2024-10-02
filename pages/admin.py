from django.contrib import admin
from .models import Product , Product_image,Category , Product_Alternative , Product_Accessories 
# Register your models here.
admin.site.register(Product)
admin.site.register(Product_image)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)


