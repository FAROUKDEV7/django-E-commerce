# Generated by Django 3.2.25 on 2024-10-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='BLauthor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='blog',
            name='BLdescription',
            field=models.TextField(default='', max_length=600, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
