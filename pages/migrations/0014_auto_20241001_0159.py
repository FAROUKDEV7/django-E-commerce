# Generated by Django 3.2.25 on 2024-09-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_hotsales',
            name='HShotsales',
        ),
        migrations.RemoveField(
            model_name='product_newarrivals',
            name='NVnewarrivals',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDbestsellers',
            field=models.BooleanField(default=False, verbose_name='best sellesrs'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDhotsales',
            field=models.BooleanField(default=False, verbose_name='hot sales'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDnewarrivals',
            field=models.BooleanField(default=False, verbose_name='new arrivals'),
        ),
        migrations.DeleteModel(
            name='Product_Bestsellers',
        ),
        migrations.DeleteModel(
            name='Product_Hotsales',
        ),
        migrations.DeleteModel(
            name='product_Newarrivals',
        ),
    ]