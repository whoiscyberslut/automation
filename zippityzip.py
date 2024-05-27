# Reading ZIP files and getting a list of files in the archive by calling the .namelist() method on the Zipfile object

import zipfile

with zipfile.Zipfile('data.zip', 'r') as zipobj:
  zipobj.namelist()

# This produces a list: `['file1.py', 'file2.py', 'file3.py', 'sub_dir/', 'sub_dir/bar.py'], containing the names of the files and directories in the archive.

# Retrieving information about the files in the archive by using the .getinfo() method
# .getinfo() returns a ZipInfo object that stores information about a single member of the archive. To get information about a file in the archive, you pass its path as an argument to .getinfo().
# Using .getinfo(), you're able to retrieve information about archive members such as the date the files were last modified, their compressed sizes, and their full filenames. 

import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
  bar_info = zipobj.getinfo('sub_dir/bar.py') 
  bar_info.file_size # accessing .file_size retrieves the file's original size in bytes

# Output: 15277

bar_info.date_time 
bar_info.compress_size
bar_info.filename

# Extract ZIP Files

import zipfile
import os

os.listdir('.')
data_zip = zipfile.ZipFile('data.zip', 'r')

# Extract a single file to the current directory 

data_zip.extract('file1.py')

# Exctact a file object for reading or writing using .extractfile(), which takes a filename or TarInfo object to extract as an argument, returning a file-like object that can be read and used

f = tar.extractfile('app.py')
f.read()
tar.close() # opened archives should always be closed after they have been read or written to. Alternatively, you can use the with statement when creating tarfile objects to automatically close the archive when done.

# Extract all files into a different directory 

data_zip.extractall(path='extract_dir/')
os.listdir('.')

data_zip.close()

# Extracting data from password protected files 

import zipfile

with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
  pwd_zip.extractall(path='extract_dir', pwd='Quish3@o')

# Creating new ZIP archives 

import zipfile

file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
with zipfile.ZipFile('new.zip', 'w') as new_zip: # to create a new ZIP archive, you open a ZipFile object in write mode ('w') and add the files you want to the archive
    for name in file_list:
      new_zip.write(name)

# NOTE: opening a ZIP file in 'w' mode erases the contents of the archive and creates a new archive

# Add files to an existing archive without deleting its current contes

import zipfile

with zipfile.ZipFile('new.zip', 'a') as new_zip: # open the ZipFile object in append mode and then add the files
  new_zip.write('data.txt')

# Opening TAR archives

import tarfile

with tarfile.open('example.tar', 'r') as tar_file:
  print(tar_file.getnames())

# Reading an uncompressed TAR file and retrieving the names of the files in it using .getnames()

import tarfile
tar = tarfile.open('example.tat', mode = 'r')
tar.getnames() # returns a list with the anmes of the archive contents

# Accessing the metadata of each entry using special attributes

for entry in tar.getmembers(): # loops through the list of files returned by .getmembers() and prints out each file's attributes (e.g. name, size, and last modified time of each of the files in the archive)
  print(entry.name)
  print(' Modified:', time.ctime(entry.mtime))
  print(' Size    :', entry.size, 'bytes')
  print()

# Example output:
'''
CONTRIBUTING.rst
 Modified: Sat Nov  1 09:09:51 2018
 Size    : 402 bytes

README.md
 Modified: Sat Nov  3 07:29:40 2018
 Size    : 5426 bytes

app.py
 Modified: Sat Nov  3 07:29:13 2018
 Size    : 6218 bytes
 '''

# Extracting a single file from a TAR archive
# Method 1: Using .extract(), passing in the filename

tar.extract('README.md')
os.lidtdir('.')

# Unpack everything from a TAR archive using .extractall()

tar.extractall(path="extracted/") # the path argument is optional 

# Creating new TAR archives

import tarfile 

file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']
with tarfile.open('packages.tar', mode='w') as tar:
  for file in filelist:
    tar.add(file)

# Read the contents of the newly created archive

with tarfile.open('packages.tar', mode='r') as t:
  for member in t.getmembers():
    print(member.name)

# Reading multiple files using fileinput to loop over the contents of one or more text files quickly and easily; fileinput gets its input from command line arguemnts passed to sys.argv by default

import fileinput

for line in fileinput.input():
  process(line)

# Using fileinput to loop over multiple files

import fileinput
import sys

files = fileinput.input()
for line in files:
  if fileinput.isfirstline():
    print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
    print()

# Example usage:
'''
$ python3 fileinput-example.py bacon.txt cupcake.txt
--- Reading bacon.txt ---
 -> Spicy jalapeno bacon ipsum dolor amet in in aute est qui enim aliquip,
 -> irure cillum drumstick elit.
 -> Doner jowl shank ea exercitation landjaeger incididunt ut porchetta.
 -> Tenderloin bacon aliquip cupidatat chicken chuck quis anim et swine.
 -> Tri-tip doner kevin cillum ham veniam cow hamburger.
 -> Turkey pork loin cupidatat filet mignon capicola brisket cupim ad in.
 -> Ball tip dolor do magna laboris nisi pancetta nostrud doner.

--- Reading cupcake.txt ---
 -> Cupcake ipsum dolor sit amet candy I love cheesecake fruitcake.
 -> Topping muffin cotton candy.
 -> Gummies macaroon jujubes jelly beans marzipan.

'''
