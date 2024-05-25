# Using the pathconf module to retrieve the maximum file name length on Linux 

import os

def get_max_filename_length_linux():
  try:
    max_length = os.pathconf('/', 'PC_NAME_MAX')
    print(f"The maximum file name length on Linux is: {max_length} characters.")
  except Exception as e:
    print(f"An error occurred: {e}")

get_max_filename_length_linux()

# Output: The maximum file name length on Linux is 255 characters.
