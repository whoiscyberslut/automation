# Filename Pattern Matching 
# Method 1: Using .endswith() and .startswith() string methods

import os
# Get .txt files
for f_name in os.listdir('some_directory'): # first, get a directory listing and then iterate over it
  if f_name.endswith('.txt'):
    print(f_name)

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
