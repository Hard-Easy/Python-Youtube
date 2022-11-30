#Code Adhyayana
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_writer = PdfFileWriter()

pdf_reader = PdfFileReader('input/sample.pdf')

for page in pdf_reader.pages:
    watermark_pdf = PdfFileReader('input/watermark.pdf')
    watermark_page = watermark_pdf.getPage(0)
    watermark_page.mergePage(page)
    pdf_writer.addPage(watermark_page)

pdf_writer.write('output.pdf')
