from django.db import models


# Create your models here.
class usermodel(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)
    gender = models.CharField(max_length=20)


class VechicleInsurance(models.Model):
    ins_name = models.CharField(max_length=30)
    Sum_Assurance = models.IntegerField()
    Premium = models.IntegerField()
    Tenure = models.IntegerField()
    category=models.CharField(max_length=50)

class HealthInsModel(models.Model):
    ins_name = models.CharField(max_length=30)
    Sum_Assurance = models.IntegerField()
    Premium = models.IntegerField()
    Tenure = models.IntegerField()
    category = models.CharField(max_length=50)

class  LifeInsModel(models.Model):
    ins_name = models.CharField(max_length=30)
    Sum_Assurance = models.IntegerField()
    Premium = models.IntegerField()
    Tenure = models.IntegerField()
    category = models.CharField(max_length=50)


class vehicleModel(models.Model):
    policy = models.CharField(max_length=40)
    holder = models.CharField(max_length=50)
    amount = models.IntegerField()
    address=models.CharField(max_length=100)
    vehicle = models.CharField(max_length=25)
    reg = models.CharField(max_length=25)
    regdate=models.DateField()
    image=models.FileField(upload_to='insapp/static')
    created=models.DateTimeField(auto_now_add=True)



class payment(models.Model):
    holder = models.CharField(max_length=50)
    price = models.IntegerField()
    email = models.EmailField()
    card = models.IntegerField()
    cvv = models.IntegerField()
    month = models.IntegerField()
    expiry = models.IntegerField()


class adminmodel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    cpassword = models.CharField(max_length=30)

class healthInsurance(models.Model):
        policy_name = models.CharField(max_length=50)
        policy_holder = models.CharField(max_length=50)
        amount = models.IntegerField()
        image = models.FileField(upload_to='insapp/static')
        age = models.IntegerField()
        gender = models.CharField(max_length=50)
        holder_status = models.CharField(max_length=50)
        date_of_birth = models.DateField()
        address = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.IntegerField()
        created=models.DateTimeField(auto_now_add=True)

class lifeInsurance(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    amount=models.IntegerField()
    dateofbirth=models.DateField()
    plan=models.CharField(max_length=50)
    height=models.CharField(max_length=3)
    weight=models.CharField(max_length=3)
    description=models.CharField(max_length=100)
    image=models.FileField(upload_to='insapp/static')
    created=models.DateTimeField(auto_now_add=True)



class helathpayment(models.Model):
    holder = models.CharField(max_length=50)
    price = models.IntegerField()
    email = models.EmailField()
    card = models.IntegerField()
    cvv = models.IntegerField()
    month = models.IntegerField()
    expiry = models.IntegerField()

class lifepayment(models.Model):
    holder = models.CharField(max_length=50)
    price = models.IntegerField()
    email = models.EmailField()
    card = models.IntegerField()
    cvv = models.IntegerField()
    month = models.IntegerField()
    expiry = models.IntegerField()



