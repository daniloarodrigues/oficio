# Generated by Django 2.0.2 on 2018-03-07 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0007_auto_20180307_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsavel',
            name='email',
        ),
    ]