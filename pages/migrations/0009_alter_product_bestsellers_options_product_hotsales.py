# Generated by Django 5.1.1 on 2024-09-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_rename_new_arrivals_product_newarrivals_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_bestsellers',
            options={'verbose_name': 'Best seller', 'verbose_name_plural': 'Best sellers'},
        ),
        migrations.CreateModel(
            name='Product_Hotsales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HShotsales', models.ManyToManyField(to='pages.product', verbose_name='Hot Sales')),
            ],
            options={
                'verbose_name': 'Hot sale',
                'verbose_name_plural': 'Hot sales',
            },
        ),
    ]