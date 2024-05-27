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

# Search for files recursively in subdirectories using glob 

import glob
for file in glob.glob('**/*.py', recursive=True): # searches for .py files in the current directory and any subdirectories 
  print(file)
  
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

# OR: call os.path.dirname() and os.path.basename(), and place their return values in a tuple:

print((os.path.dirname(p), os.path.basename(p)))

# NOTE: os.path.split() does NOT take a file path and return a list of strings of each folder. For that, use the split() string method and split on the string in os.sep
# (Note that sep is in os, NOT in os.path)!!

'/usr/bin'.split(os.sep) # returns all the paths of the path as strings; on Linux systems, the returned list of folders will begin with a blank string: ['', 'usr', 'bin']
