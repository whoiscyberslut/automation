# Filename Pattern Matching 
# Method 1: Using .endswith() and .startswith() string methods

import os
# Get .txt files
for f_name in os.listdir('some_directory'): # first, get a directory listing and then iterate over it
  if f_name.endswith('.txt'):
    print(f_name)

# Example: Exclude all the .done files from the following list: ['data.txt', 'data.done', 'data_audit.done', 'data1.trans'] 

files = [f for f in os.listdir(source_dir) if f.startswith('data') and not f.endswith('.done')]

# OR: 

files = [f for f in pl.Path.cwd().glob("data*") if f.suffix != '.done'] # or f.suffix!='.done'(?)

# OR: if there is a possibility that non-files match that glob, you can add:

files = [f for f in pl.Path("/path/to/dir").glob("data*") if f.suffix != '.done' and f.is_file()]

# Method 2: Using fnmatch.fnmatch() (supports the use of wildcards such as * and ? to match filenames)

import os
import fnmatch

for file_name in os.listdir('some_directory'/):
  if fnmatch.fnmatch(file_name, '*.txt'):
    print(file_name)

# OR: os.rename(filename, 'new_' + filename) to rename all the .txt files in the specified directory by adding a 'new_' prefix to each file name

# More advanced pattern matching 
# Example: let's suppose you want to find .txt files that contain the word data, a number between a set of underscores, and the word backup in thir filename, e.g. data_01_backup, data_02_backup, and so on.

for filename in os.listdir('.'):
  if fnmatch.fnmatch(filename, data_*_backup.txt):
    print(file_name)
    
# Method 3: Using glob.glob()
# NOTE: .glob() in the glob module works just like fnmatch.fnmatch(), but unlike fnmatch.fnmatch(), it treats files beginning with a period (.) as special!

import glob
glob.glob('*.py') # search for all Python (.py) source files in the current directory

# It also supports shell-style wildcards to match patterns:

import glob
for name in glob.glob('[0-9].txt'): $ finds all text (.txt) files that contain digits in the filename
  print(name)

# Example 1: Search for files recursively in subdirectories using glob 

import glob
for file in glob.glob('**/*.py', recursive=True): # the ** pattern means "this directory and all subdirectory recursively" will be searched for .py files
  print(file)

# Example 2: Finding file using character ranges []

print('Finding file using character ranges []:-')
print(glob.glob('./[0-9].*')) # ./ refers to the current directory, [0-9] matches any single digit from 0 to 9, which is followed by a dot and 0 or more characters of any kind

# Putting it all together, the pattern matches any file in the current directorythat: starts with a single digit, is followed by a dot and, zero or more characters of any kind

# Example output: '1.txt', '2.py', '4.hello'

# Example 3: Search for Python files (.py) in the current directory whose filenames contain any of the characters -, _, or # and print the paths of these files

import glob

char_seq = "-_#"

for spcl_char in char_seq:
  esc_set = "*" + glob.escape(spcl_char) + "*" + ".py"
  for py in glob.glob(esc_set):
    print(py)

# Output: my-script.py, another-file.py, test_script.py, example#file.py

# Example 4: Search for a folder or file in a multi-level directory 

# [] matches any character in the sequence, e.g. [psr]* matches files starting with the letter p, s, or r, whereas [!] matches any character not in the sequence, e.g. [!psr]*
# matches files not starting with the letter p, s, or r.

print('All files starting with the word march')
for item in glob.glob("sales/march*"):
  print(item)

print(glob.glob("sales/[a-f]*.txt")) # Output: ['salesbar.txt', 'saleschart.txt']
print(glob.glob("sales[2-5].*")) # Output: ['sales2.txt']

# Example 5: glob() files with multiple extensions

import glob

print("All pdf and txt files")

extensions = ('*.pdf', '*.txt')
files_list = []

for ext in extensions:
  files_list.append(glob.glob(ext))
print(files_list)

# Output: ['christmas_envelope.pdf', 'reindeer.pdf', '1.jpeg', '2.jpeg', '4.jpeg', '3.jpeg', 'abc.jpeg']

# Example 6: Using glob() with regex: searching for an employee whose name matches the user input in a folder with jpeg files of employees

import glob
import re

num = input('Enter the employee number: ')
regex = rf'[a-z_]+{num}.*'

for file in glob.glob("2020/*"):
  if re.search(regex, file):
    print("Employee Photo: ", file)

''' 
Directory contents:
2020/
    john_doe1234.jpg
    jane_doe5678.jpg
    mike_7890.jpg
    doe_john1234.png

If the user enters '1234', the script will output:

Enter the employee number: 1234
Employee Photo: 2020/john_doe1234.jpg
Employee Photo: 2020/doe_john1234.png
''''

# Example 7: Pattern-based file renaming with the glob module: replacing 'draft' with 'final' in filenames

import glob
import os

for filename in glob.glob('draft*.txt'):
  os.rename(filename, filename.replace('draft', 'final'))

# OR: you can use glob to read the content of each file and checks if the word 'profit' is present:

import glob

path = '**/*.txt'
search_word = 'profit'
final_files = []

for file in glob.glob(path, recursive=True):
  try:
    with open(file) as fp:
      data = fp.read()
      if search_word in data:
        final_files.append(file)
  except:
    print('Exception while reading file')
print(final_files)

# Output: ['salesdata_2021.txt']

print(sorted(glob.glob(path)))

# Output: ['profit_april.txt', 'profit_march.txt', 'sales_april.txt', 'sales_march.txt']

# We can sort the files based on the date and time of modification by combining the glob() method wit the getmtime() method in the os.module

import glob
import os

files = glob.glob(os.path.expanduser("*"))

# Sort by modification time (mtime) ascending and descending 
files_ascending = sorted(files, key=lambda t: os.stat(t).st_mtime)
print(files_ascending)
files_descending = sorted(files, key=lambda t:os.stat(t).st_mtime)
print(files_descending)

# Output: ['sales_april.txt', 'sales_march.txt', 'profit_april.txt', 'profit_march.txt', 'sales', 'glob_demo.py']; ['glob_demo.py', 'sales', 'profit_march.txt', 'profit_april.txt', 'sales_april.txt', 'sales_march.txt']

# Deleting files using glob() 

import glob
import os

for pdf in (glob.glob("/2020/*.pdf")):
  print("Removing ", pdf)
  os.remove(pdf)

# Output: Removing salesjune.pdf

import os
from pathlib import Path

for filename in Path.home().glob('*.rxt')
# os.unlink(filename)
  print(filename)

# OSError is one of the most common errors you might stumble upon when renaming files. This error often pops up, when the file you're trying to rename either doesn't exist 
# or you lack the necessary permissions to modify it, e.g: 

import os

try:
  os.rename('old_filename.txt', 'new_filename.txt')
except OSError as e:
  print(f'Error: {e.strerror}')

# Method 4: Using pathlib.Path.glob()

from pathlib import Path
p = Path('.')
for name in p.glob('*.p*'): # returns a generator object that points to all files in the current directory that start with the letter 'p' in their file extension 
  print(name)

list(p.glob('*')) # Makes a list from the generator 
list(p.glob('project?.docx')) # Returns 'project1.docx', 'project2.docx', but not 'project10.docs, because ? only matches to one character
list(p.glob('*.?x?')) # Returns files with any name and any three-character extension, where the middle character is in 'x'

# To use a for loop to iterate over the generator that glob() returns:

p = Path('.')
for textfilepathobj in p.glob('*.txt'):
  print(textfilepathobj) # if you want to perform some operation on every file in a directory, you can use either os.listdir(path) or p.glob('*')

# Method 5: Using pathlib.Path() for getting the different parts of a path written in a string value

p = Path('/home/user/script.py')

print(p.anchor) # Output: / 
print(p.parent) # This is a Path object, not a string; Output: /home/user
print(p.name)  # Output: script.py
print(p.stem) # Output: script
print(p.suffix) #Output: .py

# OR: use the older os.path module to do the same

os.path.dirname(path) # Output: /home/user
os.path.basename(path) # Output: script.py

# If you need a path's dir name and base name together, you can call os.path.split() to get a tuple value with these two strings:

print(os.path.split(p)) # Output: ('/home/user', 'script.py') 
'/usr/bin'.split(os.sep) # returns all the paths of the path as strings; on Linux systems, the returned list of folders will begin with a blank string: ['', 'usr', 'bin']

# OR: call os.path.dirname() and os.path.basename(), and place their return values in a tuple:

print((os.path.dirname(p), os.path.basename(p)))

# NOTE: os.path.split() does NOT take a file path and return a list of strings of each folder. For that, use the split() string method and split on the string in os.sep
# (Note that sep is in os, NOT in os.path)!!

# Method 5: Using Python's f-strings with the os.rename() function to dynamically generate new file names

import os

file_number = 1
for filename in os.listdir('directory_path'):
  if filename.endswith('.txt'):
    new_filename = f'new_file_{file_number}.txt'
    os.rename(filename, new_filename)
    file_number += 1

# Output: 'new_file_1.txt', 'new_file_2.txt', 'new_file_3.txt', and so on...



