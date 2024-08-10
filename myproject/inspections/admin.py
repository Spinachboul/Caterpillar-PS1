from django.contrib import admin
from .models import Inspection, Tire, Battery, Exterior, Brake, Engine

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['truck_serial_number', 'truck_model', 'inspector_name', 'date_time']

@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = ['position', 'pressure', 'condition']

@admin.register(Battery)
class BatteryAdmin(admin.ModelAdmin):
    list_display = ['make', 'voltage', 'condition']

@admin.register(Exterior)
class ExteriorAdmin(admin.ModelAdmin):
    list_display = ['rust_dent_damage', 'oil_leak']

@admin.register(Brake)
class BrakeAdmin(admin.ModelAdmin):
    list_display = ['fluid_level', 'front_condition', 'rear_condition']

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ['oil_condition', 'oil_color', 'brake_fluid_condition']
