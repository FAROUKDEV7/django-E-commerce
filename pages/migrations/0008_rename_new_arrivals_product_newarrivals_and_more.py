# Generated by Django 5.1.1 on 2024-09-22 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_new_arrivals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New_Arrivals',
            new_name='product_Newarrivals',
        ),
        migrations.RenameField(
            model_name='product_newarrivals',
            old_name='BSnewarrivals',
            new_name='NVnewarrivals',
        ),
    ]