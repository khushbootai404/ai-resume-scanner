from PyPDF2 import PdfReader

def extract_text(file_path):
    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    except Exception as e:
        print("PDF read error:", e)

    return text