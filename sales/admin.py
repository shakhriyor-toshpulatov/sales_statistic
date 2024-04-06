from django.contrib import admin

from sales.models import Employee, Client, Product, Order

# Register your models here.
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
