import os

class PDFScannerOCR:
    """
    Simulates a PDF Scanner with OCR capabilities.
    In a real scenario, this would use 'pytesseract' for OCR and 'PyMuPDF' or 'pdf2image'.
    """
    def __init__(self):
        self.scanned_directory = "scanned_docs"
        if not os.path.exists(self.scanned_directory):
            os.makedirs(self.scanned_directory)

    def perform_ocr(self, image_path):
        """Simulates text extraction from an 'image' file."""
        print(f"Scanning {image_path} for text...")
        # Simulated OCR result
        return f"EXTRACTED TEXT FROM {image_path}\nDate: 2023-10-27\nInvoice ID: 12345\nTotal: $500.00"

    def save_as_pdf(self, text, output_filename):
        """Simulates saving the extracted text into a searchable PDF (here a .txt for logic)."""
        filepath = os.path.join(self.scanned_directory, output_filename)
        try:
            with open(filepath, 'w') as f:
                f.write(text)
            print(f"Document saved successfully at: {filepath}")
        except IOError as e:
            print(f"Error saving file: {e}")

    def process_document(self, image_path):
        """High-level workflow for OCR scanning."""
        try:
            if not os.path.exists(image_path):
                raise FileNotFoundError("Image file not found.")
            
            extracted_text = self.perform_ocr(image_path)
            
            print("\n--- Extracted Text ---")
            print(extracted_text)
            print("----------------------\n")
            
            save_choice = input("Save as searchable document? (y/n): ")
            if save_choice.lower() == 'y':
                name = input("Enter filename (e.g., invoice_scanned.pdf): ")
                self.save_as_pdf(extracted_text, name)
                
        except Exception as e:
            print(f"Processing Error: {e}")

def main():
    scanner = PDFScannerOCR()
    print("--- PDF Scanner & OCR Tool ---")
    
    # Simulation: Create a dummy image file path
    dummy_img = "sample_invoice.png"
    with open(dummy_img, 'w') as f: f.write("binary image data")
    
    scanner.process_document(dummy_img)

if __name__ == "__main__":
    main()