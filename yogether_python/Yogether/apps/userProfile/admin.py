from django.contrib import admin
from .models import *

# @admin.register(YgUser)
# class YgUserAdmin(admin.ModelAdmin):

admin.site.register(YgUser)
admin.site.register(YgUserInfo)
admin.site.register(YgGender)
admin.site.register(YgLocation)
admin.site.register(YgMaritalStatus)
admin.site.register(YgExperience)
admin.site.register(YgDoctrine)
admin.site.register(YgTradition)
admin.site.register(YgPractice)
admin.site.register(YgInterest)
