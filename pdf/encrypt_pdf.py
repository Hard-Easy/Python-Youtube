#Code Adhyayana
from PyPDF2 import PdfFileReader, PdfFileWriter

reader = PdfFileReader("input/sample.pdf")
pdf_writer = PdfFileWriter()

for page in reader.pages:
    pdf_writer.addPage(page)

pdf_writer.encrypt("supersecret")
pdf_writer.write('encrypted-pdf.pdf')