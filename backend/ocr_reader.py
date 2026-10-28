from pdf2image import convert_from_path
import pytesseract

POPPLER_PATH = r"C:\Users\User\Downloads\poppler-26.02.0\Library\bin"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_scanned_pdf(pdf_path):
    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    full_text = ""

    for img in images:
        text = pytesseract.image_to_string(img, lang="eng")
        full_text += text + "\n"

    return full_text