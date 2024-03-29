# Generated by Django 2.0.2 on 2019-08-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado'),
        ),
    ]
