# app/reports/generate_pdf.py
import pdfkit

def generate_pdf(html_content, output_path):
    # Specify the path to the wkhtmltopdf executable
    path_to_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'  # Update this path
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    print("converted successfully")
    
    # Generate PDF from HTML content
    pdfkit.from_string(html_content, output_path, configuration=config)
