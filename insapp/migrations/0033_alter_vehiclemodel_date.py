# Generated by Django 4.1.4 on 2023-01-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0032_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
