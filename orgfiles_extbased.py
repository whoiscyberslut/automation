# Python script that organises files by categorising them based on extensions in individual directories within a parent directory 

import os
import shutil

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
      # Move the file to the corrensponding directory
      shutil.move(full_path, destdir)
  
if __name__ == '__main__':
  directory = os.getcwd()
  # directory = r"Enter your path to run this script"
  # Example:
  # directory = r"/home/user/folder"
  fileorganise(directory)
