# Generated by Django 4.2.2 on 2023-09-15 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garage',
            old_name='in_parking_available',
            new_name='is_parking_available',
        ),
    ]
