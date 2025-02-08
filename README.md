# (Smart) File Renamer

A Python script that renames files in a directory based on naming conventions and entity recognition using NLP.

## Setup

### 1. Install Dependencies

Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### 2. Download spaCy Model

This script uses `en_core_web_trf`, a transformer-based spaCy model. Install it with:

```bash
python -m spacy download en_core_web_trf
```

### 3. Usage

Run the script and follow the prompts:

```bash
python smart_rename.py
```

### 4. Naming Conventions Supported

* CamelCase
* PascalCase
* snake_case
* kebab-case
* flatcase
* UPPERFLATCASE
* Pascal_Snake_Case
* camel_Snake_Case
* SCREAMING_SNAKE_CASE
* Train-Case
* COBOL-CASE

## File Structure

```
project-folder/
│── smart_rename.py
│── clean_filename.py
│── name_conventions.py
│── requirements.txt
│── README.md
```

### Notes

* Ensure your files are in the target directory before running the script.
* Handles CamelCase splitting, number formatting, and NLP-based entity recognition for smarter renaming.
* Uses spaCy’s transformer model for improved accuracy.

Good luck renaming those files 🫡!
