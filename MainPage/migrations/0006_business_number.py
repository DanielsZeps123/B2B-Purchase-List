# Generated by Django 4.1.5 on 2023-03-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0005_rename_visible_business_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='number',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
