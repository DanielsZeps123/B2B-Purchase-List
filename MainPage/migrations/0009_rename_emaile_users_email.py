# Generated by Django 4.1.5 on 2023-03-08 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0008_business_request_tag_users_buy_sell_delete_filter_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='eMaile',
            new_name='eMail',
        ),
    ]