# Getting file attributes (e.g. file size and modified times) through os.stat(), os.scandir(), or pathlib.Path()

# Method 1: Using os.scandir() - retrieves a ScandirIterator object. Each each entry in a ScandirIterator object has a .stat() method that retrieves information about the file or directory it points to. 
# .stat() provides information such as file size and the time of last modification. 

# Example: Getting the time the files in my_directory/ were last modified. The output is in seconds:

import os

with os.scandir('my_directory/') as dir_contents:
  for entry in dir_contents:
    info = entry.stat()
    print(info.st_mtime) # Access time
    print(info.st_atime) # Modification time
    print(info.st_ctime)  # Change time
    print(info.st_birthtime) # Creation time 

def getmtime(filename):
  return os.stat(filename).st_mtime 

def getatime(filename):
  return os.stat(filename).st_atime

def getctime(filename):
  return os.stat(filename).st_ctime

    
# OR: the patlib module has corresponding methods for retrieving file information that give the same results

import os
from pathlib import Path

current_dir = Path('my_directory')

for path in current_dir.iterdir():
  info = path.stat()
  print(info.st_mtime) # Access time
  print(info.st_atime) # Modification time
  print(info.st_ctime)  # Change time
  print(info.st_birthtime) # Creation time 

# Method 2: Using os.path.getsize(path) to return the size in bytes of the file in the path argument 

import os

print(os.path.getsize('/home/user/script.py'))

# Output: 2097

# Method 3: Using the os.path function to get file timestamp

print(os.path.getatime('data/temp/test.txt')) # 1549094615.972488  
print(os.path.getmtime('data/temp/test.txt')) # 1549094615.9723485  
print(os.path.getctime('data/temp/test.txt')) # 1549094615.9723485

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

# Method 4: Convert timestamp to a datetime object representing the file's creation date

import datetime

dt = datetime.datetime.fromtimestamp(p.stat().st_ctime)
print(dt)
print(type(dt)) 

# Output: 2019-02-02 17:03:35.972348; <class 'datetime.datetime'>`

# Method 5: Getting the current timestamp and then using an f-string to create a new file name that includes the timestamp

import os
import time 

timestamp = time.strftime('%Y%m%d%H%M%S')
new_filename = f'{timestamp}_filename.txt'
os.rename('old_filename.txt', new_filename)

# Method 6: Change the file extension without modifying the filename 

import os

filename, file_extension = os.path.splitext('filename.txt')
os.rename('filename.txt', filename + '.docx')

# Method 7: Producing a list of dictionaries where each dictionary contains the path, name, and size of a file in the current working directory

import os

my_dir = os.getcwd()
files_list = [] # creates an empty list to store file information 

for entry in os.scandir(my_dir):
  file_path = entry.path
  file_name = entry.name
  file_size = entry.stat().st_size
  file_info = {'path': file_path, 'file_name': file_name, 'size': file_size}
  files_list.append(file_info)
  
print(files_list, sep='\n')

# Resources: https://strftime.org

