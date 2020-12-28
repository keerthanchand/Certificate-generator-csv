import pandas as pd
import os
import base64
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter




def make_certificate_pdf(first_name, last_name, certificate_id, class_name, section):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFontSize(40)
    can.setFont('Helvetica-Bold', 18)
    string = first_name
    string = string.upper()
    if last_name:
        can.drawString(245, 120, last_name.upper())
    can.drawString(245, 140, string)
    can.setFont('Helvetica', 12)
    can.drawString(277, 99, certificate_id)
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("orginalPdf.pdf", "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    certificate_id += ".pdf"
    path = "./data/"
    path += class_name
    path += "/"
    path += section
    path += "/"
    path += certificate_id
    outputStream = open(path, "wb")
    output.write(outputStream)
    outputStream.close()

# num = str(45)
# new_id = "SKISDS"+num.zfill(5)
#make_certificate_pdf("Rohitha", "Sree", "SKISDS10000")

df = pd.read_csv("data.csv")
print(len(df))
print (df['first_name'])
for i in range(215):
    print(i, df['first_name'][i], df['certificate_id'][i], df['Class'][i], df['Section'][i])
    make_certificate_pdf(df['first_name'][i], df['last_name'][i], df['certificate_id'][i], df['Class'][i], df['Section'][i])

