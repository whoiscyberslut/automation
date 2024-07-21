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
files = os.listdir('/path/to/folder1')
files2 = os.listdir('/path/to/folder2')
lastfile = files[-1]
temp = re.findall(r'\d+', lastfile)[0]

for i in range(int(temp), len(files2) + int(temp)): #int(temp): Converts the value stored in the variable temp (which represents the numeric part extracted from the last filename in path/to/folder1) into an integer. 
  os.rename('/path/to/folder2' + '/' + files2[i], f"/path/to/folder2/file{i}.txt")

# OR:

import os
import re

def get_highest_sequence_number(directory):
    """Extract the highest sequence number from filenames in the given directory."""
    pattern = re.compile(r'file(\d+)a\.txt')  # Regex to match file names like file1a.txt
    highest_num = 0
    
    for filename in os.listdir(directory):
        match = pattern.search(filename)
        if match:
            num = int(match.group(1))
            if num > highest_num:
                highest_num = num
                
    return highest_num

def rename_files(directory, start_number):
    """Rename files in the directory starting with start_number."""
    files = sorted(os.listdir(directory))
    
    for i, filename in enumerate(files):
        if filename.startswith('file') and filename.endswith('.txt'):
            # Extract current number and suffix from the filename
            match = re.match(r'file(\d+)([a-z]?)\.txt', filename)
            if match:
                current_number = int(match.group(1))
                suffix = match.group(2)
                
                # Generate the new filename with updated sequence number
                new_number = start_number + i
                new_filename = f"file{new_number}{suffix}.txt"
                
                # Construct the old and new file paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    folder1 = '/path/to/folder1'
    folder2 = '/path/to/folder2'
    
    # Get the highest sequence number from folder1
    highest_seq_num = get_highest_sequence_number(folder1)
    
    # Rename files in folder2 to follow the sequence
    rename_files(folder2, highest_seq_num + 1)  # Start renaming from the next number

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

# Example 7: Renaming filenames of the form `xyz.ogg.mp3` to `xyz.mp3`

for file in os.listdir("./"):
  if file.endswith(".mp3") and '.ogg' in file:
    os.rename(file, file.replace('.ogg', ''))

# Example 8: Renaming files from file1.txt, file2.txt, file3.txt => 001_file1.txt, 002_file2.txt, 003_file3.txt, and so on...

import os
import sys

def rename_files_in_directory(directory):
    # Check if the specified directory exists and is a directory
    if not (os.path.exists(directory) and os.path.isdir(directory)):
        print(f"Directory {directory} does not exist or is not a directory", file=sys.stderr)
        sys.exit(1)

    # Get all files in the directory with their full paths
    my_files = [(file, os.path.join(directory, file)) for file in os.listdir(directory) 
                if os.path.isfile(os.path.join(directory, file))]

    # Sort files by modified timestamp in reverse order (most recent first)
    sorted_files = sorted(my_files, key=lambda file: os.path.getmtime(file[1]), reverse=True)

    # Determine the number of digits needed for numbering (at least 3 digits)
    number_of_files = len(sorted_files)
    number_of_digits = max(3, len(str(number_of_files)))

    # Rename files with sequential numbers and leading zeros
    print("Renaming files...")
    for index, (old_name, fullpath) in enumerate(sorted_files):
        # Generate the new filename with leading zeros
        new_filename = f"{index + 1:0{number_of_digits}d}_{old_name}"
        new_fullpath = os.path.join(directory, new_filename)
        
        if old_name != new_filename:
            # Rename the file
            print(f"Renaming {old_name} to {new_filename}")
            os.rename(fullpath, new_fullpath)
        else:
            # Skip renaming if the file already has the desired filename
            print(f"File already has the desired filename: {old_name}. Skipping file.")

    print("Renaming complete.")

# Specify the directory to rename files
directory = "mydir"
rename_files_in_directory(directory)

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
