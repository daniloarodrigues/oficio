# Generated by Django 2.0.2 on 2018-03-08 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficio', '0008_remove_responsavel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficio',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='oficio',
            name='setor',
        ),
    ]