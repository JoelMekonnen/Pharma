from django.contrib import admin
from .models import DrugList, DrugOrder, Delivery
# Register your models here.
admin.site.register(DrugList)
admin.site.register(DrugOrder)
admin.site.register(Delivery)