# Getting file attributes (e.g. file size and modified times) through os.stat(), os.scandir(), or pathlib.Path()

# Method 1: Using os.scandir() - retrieves a ScandirIterator object. Each each entry in a ScandirIterator object has a .stat() method that retrieves information about the file or directory it points to. 
# .stat() provides information such as file size and the time of last modification. 

# Example: Getting the time the files in my_directory/ were last modified. The output is in seconds:

import os
with os.scandir('my_directory/') as dir_contents:
  for entry in dir_contents:
    info = entry.stat()
    print(info.st_mtime)

# OR: the patlib module has corresponding methods for retrieving file information that give the same results

from pathlib import Path
current_dir = Path('my_directory')
for path in current_dir.iterdir():
  info = path.stat()
  print(info.st_mtime)

# Method 2: Using os.path.getsize(path) to return the size in bytes of the file in the path argument 

import os

print(os.path.getsize('/home/user/script.py'))

# Output: 2097

# Method 3: Use os.listdir() to find the total size of all the files in a given directory

import os

totalsize = 0
for filename in os.listdir('/home/user'):
  totalsize = totalsize + os.path.getsize(os.path.join('/home/user', filename))
  
print(totalsize)

# Output: 5122383

# Converting this into a human-readable format: 

from datetime import datetime
from os import scandir

def convert_date(timestamp):
  d = datetime.utcfromtimestamp(timestamp)
  formatted_date = d.strftime('%d %b %Y')
  return formatted_date

def get_files():
  dir_entries = scandir('my_directory/')
  for entry in dir_entries:
    if entry.is_file():
      info = entry.stat()
      print(f'{entry.name} Last Modified: {convert_date(info.st_mtime)}')

# Example output: 
# >>> get_files() file1.py Last modified:  04 Oct 2018 file3.txt Last modified:  17 Sep 2018 file2.txt Last modified:  17 Sep 2018

# Resources: https://strftime.org

