# Generated by Django 4.1.4 on 2023-01-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0020_delete_quesmodel_delete_vehiclemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=40)),
                ('holder', models.CharField(max_length=50)),
                ('vehicle', models.CharField(max_length=25)),
                ('reg', models.CharField(max_length=25)),
                ('date', models.DateField()),
            ],
        ),
    ]
