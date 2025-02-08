import spacy  
import re

nlp = spacy.load("en_core_web_md")

def split_camel_case(text: str) -> str:
    """
    Splits camel case and snake case words into individual words.
    """
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Split camel case
    text = re.sub(r'[_-]', ' ', text)  # Replace underscores and hyphens with spaces
    return text

def clean_filename(filename: str) -> str:
    """
    Cleans the filename by:
    - Replacing non-alphanumeric characters (except underscores and hyphens) with spaces
    - Standardizing spaces
    """
    cleaned = re.sub(r'[^a-zA-Z0-9_-]', ' ', filename)  # Keep only alphanumeric, underscores, and hyphens
    cleaned = re.sub(r'[_-]+', ' ', cleaned)  # Replace multiple underscores/hyphens with a space
    return cleaned.strip()

def segment_filename(filename: str) -> str:
    """
    Uses spaCy to:
    - Detect words in filenames without spaces
    - Recognize named entities (if applicable)
    - Preserve all meaningful words while removing unwanted junk
    """
    cleaned = clean_filename(filename)
    split_cleaned = split_camel_case(cleaned)
    doc = nlp(split_cleaned)

    words = []
    for token in doc:
        if token.is_alpha or token.is_digit or token.ent_type_ or token.like_num:  
            words.append(token.text)

    return " ".join(words)  # Return cleaned filename with proper spacing

# Test Cases
filenames = [
    "elonMusk2024Report_final",
    "SpaceX_StarshipLaunch_v2",
    "projectApollo11_MissionData",
    "financial-report-2023$$$.pdf",
]

for fname in filenames:
    print(f"Original: {fname} -> Processed: {segment_filename(fname)}\n")