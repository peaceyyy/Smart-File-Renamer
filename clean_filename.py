import spacy  
import re

nlp = spacy.load("en_core_web_trf")

def preprocess_filename(filename: str) -> str:
    # Replace underscores & hyphens with spaces
    filename = re.sub(r'[_-]+', ' ', filename)

    # Split camel case 
    filename = re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', filename)

    # Ensure numbers are separated from letters
    filename = re.sub(r'(?<=[A-Za-z])(?=[0-9])|(?<=[0-9])(?=[A-Za-z])', ' ', filename)

    # Remove unwanted symbols 
    filename = re.sub(r'[^a-zA-Z0-9 ]', '', filename)

    return filename.strip()

def clean_filename(filename: str) -> str:
    """
    - Splits words properly
    - Recognizes named entities
    - Preserves meaningful numbers (e.g., years, model numbers)
    """
    cleaned = preprocess_filename(filename)
    doc = nlp(cleaned)

    words = []
    for token in doc:
        # Ensure we keep meaningful numbers and entities
        if token.is_alpha or token.ent_type_ or token.like_num or token.text.isdigit() or re.match(r'v\d+', token.text):
            words.append(token.text)

    return " ".join(words)  

