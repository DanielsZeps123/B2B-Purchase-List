# Generated by Django 4.1.5 on 2023-03-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0003_business_busneslogo_business_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='busnesLogo',
        ),
        migrations.AddField(
            model_name='business',
            name='bussinesLogo',
            field=models.ImageField(blank=True, null=True, upload_to='MainPage/static/images/businesses/'),
        ),
    ]
