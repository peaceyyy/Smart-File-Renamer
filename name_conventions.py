import os

def camel_case(string: str) -> str:
    words = string.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def pascal_case(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split())

def snake_case(string: str) -> str:
    return '_'.join(word.lower() for word in string.split())

def kebab_case(string: str) -> str:
    return '-'.join(word.lower() for word in string.split())

def flat_case(string: str) -> str:
    return ''.join(char.lower() for char in string if char != ' ')

def upper_flat_case(string: str) -> str:
    return ''.join(char.upper() for char in string if char != ' ')

def pascal_snake_case(string: str) -> str:
    return '_'.join(word.capitalize() for word in string.split())

def camel_snake_case(string: str) -> str: 
    words = string.split() 
    return '_'.join([words[0].lower()] + [word.capitalize() for word in words[1:]])
       
def screaming_snake_case(string: str) -> str:
    return '_'.join(word.upper() for word in string.split())

def train_case(string: str) -> str:
    return '-'.join(word.capitalize() for word in string.split())

def cobol_case(string: str) -> str:
    return '-'.join(word.upper() for word in string.split())

def apply_naming_convention(string: str, convention: str) -> str:
    selector = {
        "camelcase": camel_case,
        "pascalcase": pascal_case,
        "snake_case": snake_case,
        "kebab_case": kebab_case,
        "flatcase": flat_case,
        "upperflatcase": upper_flat_case,
        "pascal_snake_case": pascal_snake_case,
        "camel_snake_case": camel_snake_case,
        "screaming_snake_case": screaming_snake_case,
        "train_case": train_case,
        "cobol_case": cobol_case
    }
    # Normalize the convention string to match the keys in the selector
    normalized_convention = convention.lower().replace('-', '_')
    func = selector.get(normalized_convention)
    if func:
        return func(string)
    else:
        raise ValueError(f"Unknown naming convention: {convention}")
    
def rename_files_in_directory(directory: str, convention: str):
    for filename in os.listdir(directory):
        base, ext = os.path.splitext(filename)
        new_name = apply_naming_convention(base, convention) + ext
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed '{filename}' to '{new_name}'")
    
