from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(OrderProducts)
admin.site.register(Address)
