# Generated by Django 2.0.2 on 2018-03-05 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0005_remove_oficio_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficio',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
