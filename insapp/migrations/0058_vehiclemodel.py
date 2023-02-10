# Generated by Django 4.1.4 on 2023-01-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0057_delete_vehiclemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=40)),
                ('holder', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('vehicle', models.CharField(max_length=25)),
                ('reg', models.CharField(max_length=25)),
                ('regdate', models.DateField()),
                ('image', models.FileField(upload_to='insapp/static')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]