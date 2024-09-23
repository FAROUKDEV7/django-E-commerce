from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class Brand(models.Model):
    BRname=models.CharField(max_length=100,verbose_name=_('brand name'))

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.BRname



class variant(models.Model):
    VARname=models.CharField(max_length=100,verbose_name=_('variant name'))
    

    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'


    def __str__(self):
        return self.VARname
    
