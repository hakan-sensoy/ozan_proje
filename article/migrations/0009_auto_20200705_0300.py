# Generated by Django 3.0.4 on 2020-07-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20200704_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='quantity',
            field=models.TextField(verbose_name='Quantity *'),
        ),
    ]
