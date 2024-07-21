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
    print('{i:02d}_{filename}')

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

# Example 4: Renaming files with sequence number

import os

path = r'/path/to/folder'
fileseq = 1

for filename in os.listdir(path):
  os.rename(filename, 'newfilename_' + str(fileseq))
  fileseq += 1

# Example 5: Get a filename without extension using the split() function 

import os
path = '/path/to/directory/filename.exe'
print(os.path.basename(path).split('.')[0]

# Method 2: Get a filename from the path without extension using Path.stem 

import pathlib 
path = '/path/to/directory/filename.exe'
full_name = pathlib.Path(path).name
file_name = pathlib.Path(path).stem

print(full_name)
print(file_name)

# Output: file1.txt, file1

# Method 3: Get the filename from the path without extension using rfind()
# Steps to solve:
# (1) use the ntpath module
# (2) extract the base name from the file from the path and append it to a separate array
# (3) take the array generated and find the last occurrence of the '.' character in the string 
# Note: finding only the instance of '.' instead of the last occurrence may create problems if the name of the file itself contains '.'
# (4) We would find that index using rfind and then finally slice the part of the string before the index to get to the filename

import ntpath 

path = '/path/to/file/filename.exe'
filenames = []
for p in path:
  filenames.append(ntpath.basename(p))

for name in filenames:
  k = name.rfind('.')
  print(name[:k])

# OR: you can use print(path.rpatition('.')[0])
# OR: you can use splitext() to split the path name into a pair root and extension 

import os
path = '/path/to/file/filename.exe'
print(os.path.splitext(path)[0])

# Output: /path/to/file/filename

# OR: You can extract the filename from the path without the extension using the split() function
file_path = "/home/user/file1.txt"
file_name = file_path.split("/")[-1]
print(file_name) 

# Output: file1.txt

# OR: you can use the os.path.basename function to get the filename from a given path without the extension

import os

file_path = "/home/user/file1.txt"
full_name = os.path.basename(file_path)
file_name = os.path.splitext(full_name)

print(full_name)
print(file_name[0])

# Example 6: Renaming files according to the specified format - day, month, year, and the original category (e.g., Document), with the appropriate extension (.pdf or .jpg)

'''
Input(Files in the Current Directory):

2024-05-27-Document.pdf
2024-05-27-Photo.jpg
2024-05-28-Document.pdf
2024-05-28-Photo.jpg

After running the script, the files will be renamed according to the specified format. Let's assume that the fourth component in each file name represents the day, 
the second component represents the month, and the third component represents the year. The new format will be: {day}-{month}-{year}-{category}.{extension}.

Output (Renamed Files):

27-05-2024-Document.pdf
27-05-2024-Photo.jpg
28-05-2024-Document.pdf
28-05-2024-Photo.jpg
''''

import os

for file in os.listdir():
  name, ext = os.path.splitext(file)
  splitted = name.split("-")
  splitted = [s.strip() for s in splitted]
  new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0}{ext}
  os.rename(file, new name)

  # OR:

import os
from pathlib import Path

for file in os.listdir():
  f = Path(file)
  name, ext = f.stem, f.suffix
  splitted = name.split("-")
  splitted = [s.strip() for s in splitted]
  new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"
  f.rename(new_name)

# Example 7: Renaming filenames of the form `xyz.ogg.mp3` to `xyz.mp3`

for file in os.listdir("./"):
  if file.endswith(".mp3") and '.ogg' in file:
    os.rename(file, file.replace('.ogg', ''))

# OR

from pathlib import Path
for path in Path('.').glob('*.mp3'):
  if '.ogg' in path.stem:
    new_name = path.name.replace('.ogg', '')
    path.rename(path.with_name(new_name))

# Example 8: Renaming files from file1.txt, file2.txt, file3.txt => 001_file1.txt, 002_file2.txt, 003_file3.txt, and so on...

import os 
import sys

dir = "mydir"
if not (os.path.exists(dir) and os.path.isdir(dir)):
  # Write error message to stderr:
  print(f"Directory {dir} does not exist or is not a directory", file=sys.stderr)
  # Exit program with exit code 1 indicating the script has failed
  sys.exit(1)
# Get all files in the directory and store for each file it's name and the full path to the file
# This way we won't have to create the full path many times
my_files = [(file, os.path.join(dir, file)) for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]
# Sort by "modified" timestamp in reverse order => file with most recent modified date first  
# We need to use the fullpath here which is the second element in the tuple
sorted_by_creation_date = sorted(my_files, key=lambda file:os.path.getmtime(file[1]), reverse=True)
# Get number of digits required to assign a unique value
number_of_digits = len(str(len(my_files)))
# Use at least 3 digits, even if that's not actually required to uniquely assign values
number_of_digits = max(3, number_of_digits)

# Loop over all files and rename them
print("Renaming files...")
for index, (file, fullpath) in enumerate(my_files):
  # Rename files with leading zeros and start with index 1 instead of 0
  new_filename = f"File{index + 1}.txt" #f"{index + 1:0{number_of_digits}d}_{file}" #f"file{index + 1}.txt"
  if new_filename == file:
    # Move on to next file if the file already has the desired filename
    print(f"File already has the desired filename: {file}. Skipping file.")
    continue
  # Concatenate new filename with path to directory
  new_name = os.path.join(dir, new_filename)
  # Rename the file
  print(f"{file} => {new_filename}")
  os.rename(fullpath, new_name)

print("Done.")
                                 
# Example 9: Autoincrementing filenames

import os

files = [f"file_{i:05}x.txt for i in range(20)]

org = os.path.abspath("./dir1/dir2/")
new = os.path.abspath("./dir1/dir2/new/")
os.makedirs(new)

# Create all in org
for f in files:
  with open(os.path.join(org,f), "w") as f:
    f.write(" ")
    
# Create every 4th one in new 
for f in files[::4]:
  with open(os.path.join(new, f), "w") as f:
    f.write(" ")

for root, dirs, files in os.walk(org):
  print(root)
  print(" [d] ", dirs)
  print(" [f] ", sorted(files))

def save_file(old_path, new_path):
  # topdown=False allows to modify the results to NOT recurse
  for root, dirs, files in os.walk(old_path, topdown=False):
    dirs = []  # do not recurse into subdirs (whereto we copy the stuff)
    root_abs = os.path.abspath(root)
    new_abs = os.path.abspath(new_path)

    for name in sorted(files): # sorting is convenience, not needed
      old_file = os.path.join(root_abs, name)
      new_file = os.path.join(new_abs, name)

      # Fix renaming logic (simplified) - looks until a unique name is found
      i = 1
      base, extension = os.path.splitext(name)
      while os.path.exists(new_file):
        # Create a new name if it already exists 
        new_file = os.path.join(new_abs, f"{base}_{i}{extension}")
        i += 1
      
      # Do the copy over
      os.rename(old_file, new_file)

# Usage: 
# org = os.path.abspath("./dir1/dir2/")
# new = os.path.abspath("./dir1/dir2/new/")

save_file(org,new)

for root,dirs,files in os.walk(org):
    print(root)
    print(" [d] ", dirs)
    print(" [f] ", sorted(files))

# Output afterwards:

'''
/tmp/dir1/dir2
 [d]  ['new']
 [f]  []
/tmp/dir1/dir2/new
 [d]  []
 [f]  ['file_00000x.txt', 'file_00000x_1.txt', 'file_00001x.txt', 'file_00002x.txt', 
       'file_00003x.txt', 'file_00004x.txt', 'file_00004x_1.txt', 'file_00005x.txt', 
       'file_00006x.txt', 'file_00007x.txt', 'file_00008x.txt', 'file_00008x_1.txt', 
       'file_00009x.txt', 'file_00010x.txt', 'file_00011x.txt', 'file_00012x.txt', 
       'file_00012x_1.txt', 'file_00013x.txt', 'file_00014x.txt', 'file_00015x.txt', 
       'file_00016x.txt', 'file_00016x_1.txt', 'file_00017x.txt', 'file_00018x.txt', 
       'file_00019x.txt']
'''

# Example 10: Rename with incrementing numbers

import os

i = 0
while os.path.exists("sample%s.xml" % i):
  i += 1

fh = open("sample%s.xml", % i, "w")

# That should give you sample0.xml initially, then sample1.xml, etc.
