# Generated by Django 4.1.4 on 2023-01-06 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0005_vehiclemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemodel',
            name='owner',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
