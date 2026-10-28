from pypdf import PdfReader
from ocr_reader import extract_text_from_scanned_pdf

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    # If the PDF has little or no extractable text, use OCR
    if len(text.strip()) < 30:
        print("Using OCR...")
        text = extract_text_from_scanned_pdf(pdf_path)

    return text