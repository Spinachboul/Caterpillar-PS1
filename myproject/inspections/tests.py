from django.test import TestCase
from .models import Inspection

class InspectionModelTest(TestCase):

    def test_string_representation(self):
        inspection = Inspection(truck_serial_number="12345", inspector_name="John Doe")
        self.assertEqual(str(inspection), "12345 - John Doe")
