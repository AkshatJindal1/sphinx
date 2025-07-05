import fitz  # PyMuPDF library
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload-cv', methods=['POST'])
def handle_cv_upload():
    # 1. Check if a file was uploaded in the request
    if 'cv_file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['cv_file']
    
    # 2. Check if the filename is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 3. Ensure the file is a PDF
    if file and file.filename.lower().endswith('.pdf'):
        try:
            # 4. Read the file into memory and open with PyMuPDF
            pdf_document = fitz.open(stream=file.read(), filetype="pdf")
            
            # 5. Extract text from all pages
            full_text = ""
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                full_text += page.get_text()
            
            pdf_document.close()

            # 6. Now, 'full_text' is the clean string to send to the Gemini LLM
            # (Here you would call the LLM with the prompt we designed)
            
            # For demonstration, we'll just return the extracted text
            # In production, you'd return the JSON from the LLM
            return jsonify({
                "status": "success",
                "extracted_text_length": len(full_text),
                "extracted_text_preview": full_text
            })

        except Exception as e:
            return jsonify({"error": f"Failed to process PDF: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid file type, please upload a PDF"}), 400

if __name__ == '__main__':
    app.run(debug=True)