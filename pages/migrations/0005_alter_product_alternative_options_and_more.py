# Generated by Django 5.1.1 on 2024-09-22 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_product_alternative'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_alternative',
            options={'verbose_name': 'Product alternative', 'verbose_name_plural': 'Products alternative'},
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACproduct_accessories', models.ManyToManyField(related_name='product_accessories', to='pages.product', verbose_name='product accessories')),
                ('ACproduct_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_name', to='pages.product', verbose_name='product name')),
            ],
            options={
                'verbose_name': 'Accessory',
                'verbose_name_plural': 'Accessories',
            },
        ),
    ]
