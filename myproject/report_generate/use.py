# example_usage.py
from generate_report import render_html_report
from generate_pdf import generate_pdf

# Example data
report_data = {
    'header': {
        'truck_serial_number': '7301234',
        'truck_model': '730',
        'inspection_id': '001',
        'inspector_name': 'John Doe',
        'inspection_employee_id': 'EMP123',
        'date_time': '2024-08-09 10:00:00',
        'location': 'Warehouse A',
        'geo_coordinates': '12.3456, 78.9012',
        'service_meter_hours': '12345',
        'inspector_signature': 'John Doe Signature',
        'customer_name': 'ABC Corp',
        'cat_customer_id': 'CAT456'
    },
    'tires': {
        'pressure_left_front': '32 PSI',
        'pressure_right_front': '32 PSI',
        'condition_left_front': 'Good',
        'condition_right_front': 'Ok',
        'pressure_left_rear': '30 PSI',
        'pressure_right_rear': '30 PSI',
        'condition_left_rear': 'Needs Replacement',
        'condition_right_rear': 'Good',
        'summary': 'All tires are in good condition except for the left rear tire which needs replacement.',
        'images': ['download.jpeg']
    },
    'battery': {
        'make': 'CAT',
        'replacement_date': '2023-06-15',
        'voltage': '12V',
        'water_level': 'Good',
        'condition': 'No damage',
        'leak_rust': 'No',
        'summary': 'Battery is in good condition.',
        'images': ['download.jpeg']
    },
    'exterior': {
        'damage': 'No',
        'oil_leak': 'No',
        'summary': 'Exterior is in good condition.',
        'images': ['download.jpeg']
    },
    'brakes': {
        'fluid_level': 'Good',
        'condition_front': 'Good',
        'condition_rear': 'Ok',
        'emergency_brake': 'Good',
        'summary': 'Brakes are functioning well.',
        'images': ['download.jpeg']
    },
    'engine': {
        'damage': 'No',
        'oil_condition': 'Good',
        'oil_color': 'Clean',
        'brake_fluid_condition': 'Good',
        'brake_fluid_color': 'Clean',
        'oil_leak': 'No',
        'summary': 'Engine is in good condition.',
        'images': ['path/to/engine1.jpg']
    },
    'voice_of_customer': {
        'feedback': 'Customer is satisfied with the inspection.',
        'images': ['download.jpeg']
    }
}

# Generate HTML
html_content = render_html_report(report_data)

# Generate PDF
pdf_path = 'inspection_report.pdf'
generate_pdf(html_content, pdf_path)
