import fitz  # PyMuPDF library
from flask import Flask, request, jsonify

from entity_extractor.extract import extract_entity

app = Flask(__name__)

@app.route('/extract-entity', methods=['POST'])
def handle_entity_extract():
    if 'cv_file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['cv_file']
    
    try:
        prompt = extract_entity(file, "This is the description")
        return jsonify({
            "status": "success",
            "prompt_length": len(prompt),
            "prompt": prompt
        })
    except Exception as e:
        return jsonify({"error": f"Failed to process: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)