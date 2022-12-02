from django.contrib import admin
from device import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "local_id", "type", "model")
