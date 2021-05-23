from django.contrib import admin
from .models import YgUser

# @admin.register(YgUser)
# class YgUserAdmin(admin.ModelAdmin):

admin.site.register(YgUser)
