# Generated by Django 4.1.4 on 2023-01-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0060_delete_lifeinsurance'),
    ]

    operations = [
        migrations.CreateModel(
            name='lifeInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('dateofbirth', models.DateField()),
                ('plan', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=3)),
                ('weight', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='insapp/static')),
            ],
        ),
    ]