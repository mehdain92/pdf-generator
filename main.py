from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import sys
from io import BytesIO

font_config = FontConfiguration()
html_content = sys.stdin.read()
pdf_output = BytesIO()

HTML(string=html_content).write_pdf(pdf_output)

pdf_data = pdf_output.getvalue()
sys.stdout.buffer.write(pdf_data)
