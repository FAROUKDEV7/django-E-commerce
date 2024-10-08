# Generated by Django 5.1.1 on 2024-09-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDname', models.CharField(max_length=200, verbose_name='product name')),
                ('PRDdescription', models.TextField(max_length=500, verbose_name='product description')),
                ('PRDprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='product price')),
                ('PRDdiscountprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='product offer')),
                ('PRDisnew', models.BooleanField(blank=True, null=True, verbose_name='is new product')),
                ('PRDcreated', models.DateTimeField(verbose_name='product created')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
