import fitz  # PyMuPDF library
from flask import Flask, request, jsonify

from extract import extract_cv

app = Flask(__name__)

@app.route('/upload-cv', methods=['POST'])
def handle_cv_upload():
    if 'cv_file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['cv_file']
    
    try:
        full_text = extract_cv(file)
        return jsonify({
            "status": "success",
            "extracted_text_length": len(full_text),
            "extracted_text_preview": full_text
        })
    except Exception as e:
        return jsonify({"error": f"Failed to process: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)