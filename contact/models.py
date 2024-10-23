from django.db import models
from django.utils.translation import gettext_lazy  as _
# Create your models here.

class Contact(models.Model):
    CONdescription=models.TextField(max_length=200,verbose_name=_("description"),blank=True, null=True)
    # the first country
    CONcountry1=models.CharField(max_length=100,verbose_name=_("country 1"), blank=True, null=True)
    CONaddress1=models.CharField(max_length=100,verbose_name=_("address 1"), blank=True, null=True)
    CONphone_number1=models.CharField(max_length=15,verbose_name=_("phone number1"),blank=True, null=True)
    # the second country
    CONcountry2=models.CharField(max_length=100,verbose_name=_("country 2"), blank=True, null=True)
    CONaddress2=models.CharField(max_length=100,verbose_name=_("address 2"), blank=True, null=True)
    CONphone_number2=models.CharField(max_length=15,verbose_name=_("phone number2"),blank=True, null=True)


    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact US'


    def __str__(self):
        return self.CONdescription
    