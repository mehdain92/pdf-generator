from weasyprint import HTML
import sys
from io import BytesIO

html_content = sys.stdin.read()
pdf_output = BytesIO()

HTML(string=html_content).write_pdf(pdf_output)

pdf_data = pdf_output.getvalue()
sys.stdout.buffer.write(pdf_data)
