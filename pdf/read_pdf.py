#Code Adhyayana

from PyPDF2 import PdfFileReader

pdf_reader = PdfFileReader('input/scan_sample.pdf')

page_num = pdf_reader.numPages

for i in range(page_num):
    page = pdf_reader.getPage(i)
    print(page.extractText())