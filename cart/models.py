from django.db import models

# Create your models here.
class Order(models.Model):
    order_id=models.IntegerField()
    order_completed=models.BooleanField

