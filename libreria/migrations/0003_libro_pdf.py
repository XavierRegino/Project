# Generated by Django 4.2.1 on 2023-05-28 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_rename_description_libro_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdfs/', verbose_name='PDF'),
        ),
    ]