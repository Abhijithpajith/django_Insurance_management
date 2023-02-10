from django.contrib import admin
from .views import *
from .models import *
# Register your models here.
admin.site.register(usermodel)
admin.site.register(VechicleInsurance)
# admin.site.register(vehicleModel)
# admin.site.register(payment)
admin.site.register(adminmodel)
admin.site.register(lifepayment)
admin.site.register(payment)
admin.site.register(HealthInsModel)


