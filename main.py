from fpdf import FPDF
from pathlib import Path
import time
import os

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=15)

txtFile = "/Users/jamesfrys/Documents/CS 361/video_transcriber/lib/transcribed_file.txt"
pdfFile = "/Users/jamesfrys/Documents/CS 361/video_transcriber/lib/output.pdf"

txtPath = Path(txtFile)
pdfPath = Path(pdfFile)

if txtPath.is_file():
    file = open(txtFile, "w")
    file.close()

if pdfPath.is_file():
    os.remove(pdfFile)

cur = 0
while True:
    try:
        with open(txtFile) as f:
            f.seek(0, 2)
            if f.tell() < cur:
                f.seek(0, 0)
            else:
                f.seek(cur, 0)
            for line in f:
                pdf.cell(200, 10, txt=line, ln=1, align='C')
                pdf.output(pdfFile)
            cur = f.tell()
    except IOError as e:
        pass
    time.sleep(1)