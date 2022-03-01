from fpdf import FPDF
from pathlib import Path
import time
import os

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=15)

txtFile = "/Users/jamesfrys/Documents/CS 361/video_transcriber/lib/transcribed_file.txt"
pdfFile = "/Users/jamesfrys/Documents/CS 361/video_transcriber/lib/output.pdf"

pdfPath = Path(pdfFile)

if pdfPath.is_file():
    os.remove(pdfFile)

cur = 0
while cur == 0:
    try:
        with open(txtFile) as f:
            contents = f.readlines()
            for line in contents:
                pdf.cell(200, 10, txt=line, ln=2, align='C')
            for line in contents:
                pdf.cell(0, 0, txt='', ln=0, align='C')
                pdf.output(pdfFile)
                cur += 1
    except IOError as e:
        pass
    time.sleep(1)
