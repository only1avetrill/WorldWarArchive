# Generated by Django 4.0.5 on 2022-06-08 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_document_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
    ]
