# Generated by Django 3.0.8 on 2020-09-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='created',
            field=models.DateField(auto_now_add=True, default=20200912100000, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='updated',
            field=models.DateField(auto_now_add=True, default=20200912100000, verbose_name='Fecha de actualización'),
            preserve_default=False,
        ),
    ]
