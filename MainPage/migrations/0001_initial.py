# Generated by Django 4.1.5 on 2023-03-10 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('login', models.DateTimeField(blank=True, default=None, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('date', models.DateTimeField(blank=True, default=None, null=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainPage.business')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default=None, max_length=50)),
                ('business', models.BooleanField(default=True)),
                ('sell', models.BooleanField(default=True)),
                ('buy', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainPage.request')),
                ('image', models.ImageField(blank=True, null=True, upload_to='MainPage/static/images/buy')),
            ],
            bases=('MainPage.request',),
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainPage.request')),
                ('image', models.ImageField(blank=True, null=True, upload_to='MainPage/static/images/sell/')),
                ('price', models.FloatField(blank=True, default=None, null=True)),
            ],
            bases=('MainPage.request',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('business_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainPage.business')),
                ('password', models.CharField(default=None, max_length=100)),
                ('eMail', models.EmailField(default=None, max_length=254)),
                ('surname', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
            bases=('MainPage.business',),
        ),
        migrations.AddField(
            model_name='request',
            name='tags',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainPage.tag'),
        ),
    ]
