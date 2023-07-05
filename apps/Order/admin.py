from django.contrib import admin
from apps.Order.models import Order,Items_Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Items_Order)