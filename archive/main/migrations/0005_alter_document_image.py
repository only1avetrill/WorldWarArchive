# Generated by Django 4.0.5 on 2022-06-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_document_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
    ]