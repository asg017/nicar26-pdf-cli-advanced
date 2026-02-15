import pdfplumber

pdf = pdfplumber.open("samples/ca-warn-report.pdf")
print(pdf.pages[0].extract_text())