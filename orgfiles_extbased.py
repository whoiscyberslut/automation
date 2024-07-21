# Python script that organises files by categorising them based on extensions in individual directories within a parent directory 

import os
import shutil
import sys

def fileorganise(directory):
    for element in os.listdir(directory):
        full_path = os.path.join(directory, element)
        if os.path.isfile(full_path):
            # Split the file based on the '.' delimiter and extract the last part
            parts = element.split(".")
            file_extension = parts[-1]
            # Create directory if not exists
            destdir = os.path.join(directory, file_extension)
            os.makedirs(destdir, exist_ok=True) # suppresses OSError if the directory already exists
            # Move the file to the corresponding directory
            shutil.move(full_path, destdir)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if not os.path.isdir(directory):
        print(f"The specified path {directory} is not a valid directory.")
        sys.exit(1)

    fileorganise(directory)
