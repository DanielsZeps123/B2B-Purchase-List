# Generated by Django 4.1.5 on 2023-03-10 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0006_business_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='number',
            new_name='phone',
        ),
    ]
