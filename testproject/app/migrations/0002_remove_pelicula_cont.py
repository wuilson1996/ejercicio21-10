# Generated by Django 3.2 on 2024-10-21 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='cont',
        ),
    ]
