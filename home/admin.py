from django.contrib import admin
from .models import userdata, locationdata, authoritydata

@admin.register(userdata)
class userdataAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'mypoints', 'mycredits')
    ordering = ('mycredits',)

@admin.register(locationdata)
class locationdataAdmin(admin.ModelAdmin):
    list_display = ('location', 'contributor')

@admin.register(authoritydata)
class authoritydataAdmin(admin.ModelAdmin):
    list_display = ('area', 'users')
    ordering = ('users',)
