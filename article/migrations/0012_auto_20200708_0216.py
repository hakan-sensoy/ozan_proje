# Generated by Django 3.0.4 on 2020-07-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200705_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proje',
            name='location_box',
            field=models.CharField(blank=True, choices=[('URM1', 'URI Prep & Ship - Montgomery,AL')], default='URI Prep & Ship - Montgomery,AL', max_length=25),
        ),
    ]
