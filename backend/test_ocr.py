from ocr_reader import extract_text_from_scanned_pdf

pdf_path = "../uploads/DAA NOTES UNIT 5.pdf"

text = extract_text_from_scanned_pdf(pdf_path)

print("\n========== OCR RESULT ==========\n")
print(text)
print("\n========== END ==========\n")