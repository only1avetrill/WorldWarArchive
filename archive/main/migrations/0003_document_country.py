# Generated by Django 4.0.5 on 2022-06-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_country_alter_category_options_document_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.country', verbose_name='Страна'),
            preserve_default=False,
        ),
    ]
