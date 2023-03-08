# Generated by Django 4.1.5 on 2023-03-08 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0012_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='buy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainPage.buy'),
        ),
        migrations.AlterField(
            model_name='business',
            name='login',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='sell',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainPage.sell'),
        ),
        migrations.AlterField(
            model_name='business',
            name='surname',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='product',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='tags',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainPage.tag'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]