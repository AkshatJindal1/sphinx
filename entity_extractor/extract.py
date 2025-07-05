from pathlib import Path

from cv_extractor.extract import extract_cv
from prompt_creator.fill_prompt import fill_content

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

def fill_entity_extraction_prompt(cv_file, job_description):
    cv_text = extract_cv(cv_file)
    curr_dir = Path(__file__).parent
    prompt_path = curr_dir.parent / "prompts" / "entity_extraction.txt"
    return fill_content(prompt_path, cv_text, job_description)

def extract_entity(cv_file, job_description):
    prompt = fill_entity_extraction_prompt(cv_file, job_description)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        if response_text.startswith("```json") and response_text.endswith("```"):
            response_text = response_text[7:-3].strip()
        
        return json.loads(response_text)
    except Exception as e:
        print(f"Error extracting info: {e}")
        print(f"Model raw output: {response.text}")
        return None
    
        
        