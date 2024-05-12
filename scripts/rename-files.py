import os
import re

def rename_files(directory):
    # Get all files in the directory
    files = os.listdir(directory)

    # Define the regex pattern to match filenames with digits and .jpg extension
    pattern = re.compile(r"\b\d+\.jpg\b")

    # Filter out files that already follow the desired pattern
    files_to_rename = [file for file in files if not pattern.match(file)]

    # Determine the maximum number of digits needed for padding
    max_digits = len(str(len(files_to_rename)))

    # Rename the files
    for i, file in enumerate(files_to_rename, start=1):
        # Generate the new filename with sequential numbers and appropriate padding
        new_filename = f"{i:05d}.jpg"

        # Check for duplicates
        if new_filename in files:
            print(f"Skipping duplicate file: {file}")
            continue

        # Rename the file
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed file: {file} -> {new_filename}")
    
    # return amount of files renamed
    return len(files_to_rename)

directory = "data/images/jpg"
renamed = rename_files(directory)
print(f"Files renamed in directory: {renamed}")