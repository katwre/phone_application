from django.contrib import admin
from phone_application.phone_app.models import *


class ProductAdmin(admin.ModelAdmin):
        list_display = ('pk','key','value')
        
admin.site.register(Product,ProductAdmin)