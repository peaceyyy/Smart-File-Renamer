def rename_files_in_directory(directory: str, convention: str):
    for filename in os.listdir(directory):
        base, ext = os.path.splitext(filename)
        new_name = apply_naming_convention(base, convention) + ext
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed '{filename}' to '{new_name}'")
    
