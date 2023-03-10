# Generated by Django 4.1.4 on 2023-01-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0062_lifeinsurance_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='helathpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('card', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('month', models.IntegerField()),
                ('expiry', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lifepayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('card', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('month', models.IntegerField()),
                ('expiry', models.IntegerField()),
            ],
        ),
    ]
