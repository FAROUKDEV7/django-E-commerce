# Generated by Django 3.2.25 on 2024-10-03 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_alter_product_prddiscountprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRDbase_productimage',
        ),
    ]