from django import forms
from .models import *
import datetime



class regform(forms.Form):
    name = forms.CharField(max_length=25)
    address = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    password = forms.CharField(max_length=25)
    confirm_password = forms.CharField(max_length=25)
    gender = forms.CharField(max_length=20)

class logform(forms.Form):
    email = forms.EmailField()
    password=forms.CharField(max_length=25)

class vehicleform(forms.ModelForm):
    class Meta:
        model=VechicleInsurance
        fields="__all__"


#
class vehicleDeatails(forms.Form):
    policy = forms.CharField(max_length=40)
    holder = forms.CharField(max_length=50)
    amount = forms.IntegerField()
    address=forms.CharField(max_length=100)
    vehicle = forms.CharField(max_length=25)
    reg = forms.CharField(max_length=25)
    regdate=forms.DateField()
    image=forms.FileField()



class paymentform(forms.Form):
    holder = forms.CharField(max_length=50)
    price = forms.IntegerField()
    email = forms.EmailField()
    card=forms.IntegerField()
    cvv=forms.IntegerField()
    month=forms.IntegerField()
    expiry=forms.IntegerField()

class adminform(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

class adlog(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=30)

class quesform(forms.Form):
   name=forms.CharField(max_length=50)
   question=forms.CharField(max_length=50)




class healthform(forms.Form):
    policy_name=forms.CharField(max_length=50)
    policy_holder=forms.CharField(max_length=50)
    amount=forms.IntegerField()
    image=forms.FileField()
    age=forms.IntegerField()
    gender=forms.CharField(max_length=50)
    holder_status=forms.CharField(max_length=50)
    date_of_birth=forms.DateField()
    address=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()



class lifeForm(forms.Form):
    name=forms.CharField(max_length=50)
    address=forms.CharField(max_length=100)
    phone=forms.IntegerField()
    amount=forms.IntegerField()
    email=forms.EmailField()
    dateofbirth=forms.DateField()
    plan=forms.CharField(max_length=50)
    height=forms.CharField(max_length=3)
    weight=forms.CharField(max_length=3)
    description=forms.CharField(max_length=100)
    image=forms.FileField()


class contactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Messeage= forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows':3,'cols':30}))