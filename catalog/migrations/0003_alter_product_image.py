# Generated by Django 4.2.4 on 2023-08-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_date_of_creation_product_last_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение'),
        ),
    ]
