# Generated by Django 4.1.4 on 2023-01-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insapp', '0069_delete_healthinsurance_delete_helathpayment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='healthInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=50)),
                ('policy_holder', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('image', models.FileField(upload_to='insapp/static')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('holder_status', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
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
                ('created', models.DateTimeField(auto_now_add=True)),
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
        migrations.CreateModel(
            name='payment',
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
