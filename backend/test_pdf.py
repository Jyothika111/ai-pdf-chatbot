from pdf_reader import extract_text

text = extract_text("../uploads/sample.pdf")

print(text[:1000])