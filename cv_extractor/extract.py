import fitz  # PyMuPDF library

def extract_cv(file) -> str:
    if file.filename == '':
        raise NameError("No selected file")

    # 3. Ensure the file is a PDF
    if file and file.filename.lower().endswith('.pdf'):
        try:
            # 4. Read the file into memory and open with PyMuPDF
            pdf_document = fitz.open(stream=file.read(), filetype="pdf")
            
            # 5. Extract text from all pages
            full_text = ""
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                full_text += page.get_text()    # type: ignore 
            pdf_document.close()
            return full_text
        except Exception as e:
            raise e
    else:
        raise ValueError("File not of type PDF")
            