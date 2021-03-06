# Generated by Django 3.2.6 on 2021-08-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sku', models.CharField(max_length=150, unique=True)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('quantity', models.IntegerField()),
                ('slug', models.SlugField()),
                ('consulted', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
