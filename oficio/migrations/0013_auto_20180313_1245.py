# Generated by Django 2.0.2 on 2018-03-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0012_auto_20180313_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficio',
            name='numero',
            field=models.IntegerField(),
        ),
    ]