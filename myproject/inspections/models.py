from django.db import models

class Inspection(models.Model):
    truck_serial_number = models.CharField(max_length=50)
    truck_model = models.CharField(max_length=50)
    inspector_name = models.CharField(max_length=100, blank=True, null=True)
    inspection_employee_id = models.CharField(max_length=50, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    geo_coordinates = models.CharField(max_length=100, blank=True, null=True)
    service_meter_hours = models.FloatField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    cat_customer_id = models.CharField(max_length=50, blank=True, null=True)
    overall_summary = models.TextField(blank=True, null=True)
    voice_of_customer = models.TextField(blank=True, null=True)
    report_generated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.truck_serial_number} - {self.inspector_name}'
    

class InspectionResult(models.Model):
    section = models.CharField(max_length=100)
    text_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Section: {self.section}, Result: {self.text_result}"



class Tire(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)  # e.g., "Left Front"
    pressure = models.FloatField()
    condition = models.CharField(max_length=50)  # e.g., "Good", "Ok", "Needs Replacement"
    image_path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.position} - {self.condition}'


class Battery(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    replacement_date = models.DateTimeField(blank=True, null=True)
    voltage = models.FloatField()
    water_level = models.CharField(max_length=50)  # e.g., "Good", "Ok", "Low"
    condition = models.CharField(max_length=50)
    leak_rust = models.BooleanField(default=False)
    image_path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.make} - {self.voltage}V'


class Exterior(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    rust_dent_damage = models.BooleanField(default=False)
    oil_leak = models.BooleanField(default=False)
    image_path = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Rust/Damage: {self.rust_dent_damage}'


class Brake(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    fluid_level = models.CharField(max_length=50)
    front_condition = models.CharField(max_length=50)
    rear_condition = models.CharField(max_length=50)
    emergency_brake_condition = models.CharField(max_length=50)
    image_path = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Fluid Level: {self.fluid_level}'


class Engine(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    rust_dent_damage = models.BooleanField(default=False)
    oil_condition = models.CharField(max_length=50)
    oil_color = models.CharField(max_length=50)
    brake_fluid_condition = models.CharField(max_length=50)
    brake_fluid_color = models.CharField(max_length=50)
    oil_leak = models.BooleanField(default=False)
    image_path = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Oil Condition: {self.oil_condition}'
