from pathlib import Path

from cv_extractor.extract import extract_cv
from prompt_creator.fill_prompt import fill_content

def extract_entity(cv_file, job_description):
    cv_text = extract_cv(cv_file)
    curr_dir = Path(__file__).parent
    prompt_path = curr_dir.parent / "prompts" / "entity_extraction.txt"
    return fill_content(prompt_path, cv_text, job_description)
    
        
        