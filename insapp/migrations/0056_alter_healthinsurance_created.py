# Generated by Django 4.1.4 on 2023-01-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0055_healthinsurance_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthinsurance',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]