# Generated by Django 4.1.5 on 2023-03-07 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0006_section_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='link',
        ),
    ]