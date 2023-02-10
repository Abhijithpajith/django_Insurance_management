from django.urls import path
from .views import *

urlpatterns=[
    path('index',index),
    path('registraion/',registration),
    path('login/',login),
    path('add/',vehicle),
    path('show/',show),
    path('apply/<int:id>',apply),
    path('adminVehicle/',admin_vehicle_show),
    path('payment/<str:ho>/<int:amount>',pay),
    path('showpay/<int:id>',viewpay),
    path('message/',messeage),
    path('usernav/',usernav),
    path('profile/',pro),
    path('adminreg/',adminreg),
    path('adminlogin/',adminlogin),
    path('adminshow/',adminshow),
    path('policydelete/<int:id>',delete),
    path('adminindex/',adminindex),
    path('footer/',footerview),
    path('adminnav/',adminnav),
    path('usershow/',useredit),
    path('userdelete/<int:id>',userdelete),
    path('health/<int:id>',health),
    path('payh/<str:ph>/<str:am>',payh),
    path('adminhlth/',admin_health_show),
    path('lifeins/<int:id>',life),
    path('admin_life_show/',admin_life_show),
    path('lifepayment/<str:na>/<str:au>',lifepay),
    path('logout/',logout_view),
    path('lifepayshow/<int:id>',lifepayshow),
    path('healthpaymentshow/<int:id>',health_payment_show),
    path('lifepolicy/',lifepolicy),
    path('healthpolicy/',healthpolicy),
    path('adminshow2/',adminshow2),
    path('healthdelete/<int:id>',healthdelete),
    path('adminshow3/',adminshow3),
    path('lifedelete/<int:id>',lifedelete),
    path('admin_policy/',adminpolicy),
    path('policy_holder/',admin_holder_list),
    path('contact/',contact)


]


