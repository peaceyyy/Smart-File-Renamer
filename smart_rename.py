from clean_filename import clean_filename as clean
from name_conventions import *
import os

def rename_files_in_directory(directory: str, convention: str):
    for filename in os.listdir(directory):
        base, ext = os.path.splitext(filename)
        cleaned_base = clean(base)
        new_name = apply_naming_convention(cleaned_base, convention) + ext
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"\nRenamed '{filename}' to '{new_name}'")
    
def main():
    directory = input("Enter the folder directory path: ")
    conventions = {
        "CamelCase": "camelcase",
        "PascalCase": "pascalcase", 
        "snake_case": "snake_case",
        "kebab-case": "kebab-case",
        "flatcase": "flatcase",
        "UPPERFLATCASE": "upperflatcase",
        "Pascal_Snake_Case": "pascal_snake_case",
        "camel_Snake_Case": "camel_snake_case",
        "SCREAMING_SNAKE_CASE": "screaming_snake_case",
        "Train-Case": "train-case",
        "COBOL-CASE": "cobol-case"
    }

    print("Choose a naming convention:")
    convention_keys = list(conventions.keys())
    for i, convention in enumerate(convention_keys, 1):
        print(f"{i}. {convention}")

    try:
        choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= choice < len(convention_keys):
            selected_convention = conventions[convention_keys[choice]]
            rename_files_in_directory(directory, selected_convention)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    main()