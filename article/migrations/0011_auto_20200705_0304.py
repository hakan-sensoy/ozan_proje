# Generated by Django 3.0.4 on 2020-07-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20200705_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='product_code',
            field=models.IntegerField(verbose_name='Asin or upc *'),
        ),
    ]
