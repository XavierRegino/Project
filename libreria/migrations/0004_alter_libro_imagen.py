# Generated by Django 4.2.1 on 2023-05-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_libro_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media/imagenes/', verbose_name='Imagen'),
        ),
    ]