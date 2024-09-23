from django.contrib import admin
from .models import Product , Product_image,Category , Product_Alternative , Product_Accessories , Product_Bestsellers , product_Newarrivals,Product_Hotsales
# Register your models here.
admin.site.register(Product)
admin.site.register(Product_image)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
admin.site.register(Product_Bestsellers)
admin.site.register(product_Newarrivals)
admin.site.register(Product_Hotsales)

