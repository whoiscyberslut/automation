# Example 1: Rename files in a directory from (test.jpeg, test1.jpeg, test2.jpeg) to (People-000, People-001, People-002 and so on).

import os

src = '/path/to/directory'
ext = '.txt'
for i filename in enumerate(os.listdir(src):
  if filename.endswith(ext):
      os.rename(filename, src+'People-' + str(i).zfill(3)+ext)

# Example 2: Add incresing numbers to filenames in a directory sorted by date, e.g. add "01_", "02_", "03_" to the following files: test1.txt (oldest text file), 
# test2.txt, test3.txt, text4.txt (newest text file).

# Solution 1: if you want to number the files by age, they need to be sorted first; you call sorted and pass a key paramter; the function os.path.getmtime will 
# sort in ascending order of age (oldest to latest). Steps to recreate:
# 1. Use glob.glob to get all text files in a given directory.
# 2. Use str.zfill to strings of the form 0x_.
# 3. Use os.rename to rename the titles.

import glob 
import os 

sorted_files = sorted(glob.glob('/path/to/directory/*.txt'), key=os.get.getmtime) 
# The key parameter specifies a function to be called on each list element prior to making comparisons for sorting.
# key=os.path.getmtime means that for each file in the list, os.path.getmtime is called to get the modification time, and the files are then sorted based on these modification times.

for index, file in enumerate(sorted_files, 1): # Loops through the sorted list of files with an index starting from 1.
  try:
    head, tail = os.path.split(file) # Splits a file path into its directory part (head) and the file name part (tail).
    os.rename(f, os.path.join(head, str(i).zfill(2) + '_' + tail))
  except OSError:
      print('Invalid operation') # If an error occurs due to insufficient permissions, file not found, or other file-related issues.

# Faster method:

for i, filename in enumerate(glob.glob('/path/to/directory/*.txt'), start=1):
    print('{:02d}_{}'.format(i, filename))

# Without list comprehension 
# Note: {0:02d} is a format specifier that ensures that the value of i is printed with at least two digits, zero-padded if necessary (e.g., 01, 02, ..., 09, 10, ...).

import os
i = 1
for file in os.listdir('/path/to/directory'):
  if file.endswith('.txt'):
    print('{0:02d}'.format(i) + '_' + file)
    i += 1

  # Example 3: Rename a file sequence in folder 2, such that they are in sequence with files in folder 1 - i.e.
  '''
  folder1/
    file1a.txt
    file1b.txt
    file1c.txt
    file2a.txt
    file2b.txt
    file2c.txt
    file3a.txt
    file3b.txt
    file3c.txt
    file4a.txt
    file4b.txt
    file4c.txt
    file5a.txt
    file5b.txt
    file5c.txt

  folder2/
    file1a.txt
    file1b.txt
    file1c.txt
    file2a.txt
    file2b.txt
    file2c.txt
    file3a.txt
    file3b.txt
    file3c.txt
    file4a.txt
    file4b.txt
    file4c.txt
    file5a.txt
    file5b.txt
    file5c.txt

  must become:

  folder2/
    file6a.txt
    file6b.txt
    file6c.txt
    file7a.txt
    file7b.txt
    file7c.txt
    file8a.txt
    file8b.txt
    file8c.txt
    file9a.txt
    file9b.txt
    file9c.txt
    file10a.txt
    file10b.txt
    file10c.txt
'''

import os
import re
files = os.listdir(/path/to/folder1)
files2 = os.listdir(/path/to/folder2)
lastfile = files = [-1]
temp = re.findall(r'\d+', lastfile)[0]

for i in range(int(temp), len(files2) + int(temp)): #int(temp): Converts the value stored in the variable temp (which represents the numeric part extracted from the last filename in path/to/folder1) into an integer. 
  os.rename('/path/to/folder2' + '/' + files2[i], f"/path/to/folder2/file{i}.txt")

  
