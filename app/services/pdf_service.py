from pypdf import PdfReader

def extract_pdf_text(file_path: str):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return {
        "pages": len(reader.pages),
        "text": text,
        "characters": len(text)
    }