def fill_content(file_path, cv_text, jd_text):
    """
    Reads a text file, replaces a placeholder, and returns the modified content.

    Args:
        file_path: The path to the text file.
        cv_text: The text to fill into the placeholder cv_text.
        jd_text: The text to fill into the placeholder jd_text.

    Returns:
        The content of the file with the placeholder filled in.
    """
    with open(file_path, 'r') as f:
        prompt_template = f.read()
        
    return prompt_template.replace("{{cv_text}}", cv_text).replace("{{jd_text}}", jd_text)