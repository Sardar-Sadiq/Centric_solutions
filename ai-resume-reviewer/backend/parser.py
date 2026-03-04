from pdfminer.high_level import extract_text

def get_pdf_text(filepath):
    """Simple file handling to extract text from a PDF."""
    try:
        return extract_text(filepath)
    except Exception as e:
        print(f"Error: {e}")
        return None