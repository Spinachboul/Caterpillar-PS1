# app/reports/generate_report.py
from jinja2 import Environment, FileSystemLoader
import os

def render_html_report(report_data):
    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    template = env.get_template('inspection_report.html')
    
    # Render the HTML report with the given data
    html_content = template.render(report_data)
    
    return html_content
