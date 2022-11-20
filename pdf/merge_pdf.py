#Code Adhyayana

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

pdf_writer = PdfFileWriter()

pdf_reader = PdfFileReader('input/sample.pdf')
pdf_number_pages = pdf_reader.numPages

for i in range(pdf_number_pages):
    page = pdf_reader.getPage(i)
    pdf_writer.addPage(page)

pdf_reader = PdfFileReader('input/sample_diff_format.pdf')
pdf_number_pages = pdf_reader.numPages

for i in range(pdf_number_pages):
    page = pdf_reader.getPage(i)
    pdf_writer.addPage(page)

pdf_writer.write('output.pdf')
