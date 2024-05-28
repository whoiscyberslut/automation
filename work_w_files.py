# Working with files in Python 

# Python's "with open(...) as ..." Pattern

try:
  with open('data.txt', 'r') as f:
    data = f.read()
except FileNotFoundError:
  print("The file does not exist.")f
except PermissionError:
  print("Permission denied.")

# IOError: related to input and output that include file-related issues; FileAlreadyExistsError: create a file that already exists

# OR: you can use the readlines() method to get a LIST of string values from the file, one string for each line of text:
  data = f.readlines()
  print(data)
  
with open('data.txt', 'r') as f:
  f.write(data)

# Directory listing 
# Method 1: Using os.listdir() - os.listdir() returns a Python list containing the names of the files and subdirectories in the directory given by the path argument

import os
entries = os.listdir('my_directory')
for entry in entries:
  print(entry)

# Find files in the current directory (but not subdirectories)

for file in os.listdir("/root"):
	if file.startswith("art"):
		print(file)

# VS

# Find files recursively 

for path, currentDirectory, files in os.walk("/root"):
	for file in files:
		if file.startswith("art"):
			print(file)

# Output: article 1.rtf

# Method 2: Using os.scandir() - os.scandir() returns an iterator

import os

with os.scandir('my_directory/') as entries:
  for entry in entries:
    print(entry.name) # prints out the filenames in my_directory/

# Method 3: Using pathlib module's .iterdir() module - creates an iterator of all files and folders in a directory. Each entry yielded by .iterdir() contains information 
# about the file or directory, such as its name and file attributes.

from pathlib import Path
entries = Path('my_directory/')
for entry in entries.iterdir():
  print(entry)

# Note: These functions return a list of _everything_ in the directory, including subdirectories!

# Listing all files in a directory
# Method 1: Using os.listdir()

import os

basepath = '.'
for entry in os.listdir(basepath):
  if os.path.isfile(os.path.join(basepath, entry)):
    print(entry)

# Method 2: Using os.scandir() 

import os 

basepath = 'my_directory/'
with os.scandir(basepath) as entries:
  for entry in entries:
    if entry.is_file():
      print(entry.name)

# Method 3: Using pathlib.Path()

from pathlib import Path
basepath = Path('my_directory/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
  if item.if_file():
    print(item.name)

# OR: 

from pathlib import Path
basepath = Path('my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
  print(item.name)

# Listing subdirectories 
# Method 1: Using os.listdir()

import os
basepath = 'my_directory/'
for entry in os.listdir(basepath):
  if os.path.isdir(os.path.join(basepath, entry)):
    print(entry)

# Method 2: Using os.scandir()

import os
basepath = 'my_directory' 
with os.scandir(basepath) as entries:
  for entry in entries:
    if entry.is_dir():
      print(entry.name)

# Method 2: Using pathlib.Path()

from pathlib import Path 
basepath = Path('my_directory/')
for entry in basepath.iterdir():
  if entry.is_dir():
    print(entry.name)

# Making directories using os and pathlib modules 
# Example 1: Creating a single directory - pass a path to the directory as a parameter to os.():

import os 
try:
  os.mkdir('example_directory/')
  os.mkdir('testdir', 755) # it can take a second parameter to specify permissions
  print("The directory has been created successfully")
except FileExistsError: # you can use an 'if os.path.exists(path): os.mkdir("path")' statement 
  print("The directory names " + path + " already exists.")

# If a directory already exists, os.mkdir() raises FileExistsError. Alternatively, you can create a directory using pathlib:

from pathlib import Path 
p = Path('example_directory/')
p.mkdir()

# If the path already exists, mkdir() raises a FileExistsError. To avoid errors like this, catch the error when it happens and let your user know: 

from pathlib import Path
p = Path('example_directory/')
try:
  p.mkdir()
except FileExistsError as exc:
  print(exc)

# OR:

from pathlib import Path 

p = Path('example_directory/')
p.mkdir(exist_ok=True) # this will not raise an error if the directory already exists

# Creating multiple directories

import os
os.makedirs(2018/10/05, mode=0o770) # creates the 2018/10/05 directory structure and gives the owner and group users read, write and execute permissions (NOT TESTED!)
os.makedirs('testdir2/something/somethinselse', 755)

# Method 2: Use .mkdir() from pathlib.Path:

import pathlib 
p = pathlib.Path('2018/10/05')
p.mkdir(parents=True)

# Traversing Directories and Processing Files 

# Method 1: Using os.walk() - either top-down or bottom-up

os.walk("/etc/grub.d")
list(os.walk("/etc/tuned")) # Output: [('/etc/grub.d', [], ['10_linxxx])]

for dirpath, dirnames, files in os.walk('.'): # walks a directory tree and prints the names of the directories and files 
  print(f'Found directory: {dirpath}')
  for file_names in files:
    print(file_name)

# OR: to traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk():

for dirpath, dirnames, files in os.walk('.', topdown=False): # passing the topdown=False argument will make os.walk() print out the files it finds in the subdirectories before listing the contents of the root directory
  print(f'Found directory: {dirpath}')
  for file_name in files:
    print(file_name)

# By default, os.walk() does not walk down into symbolic links that resolve to diretories. This behaviour can be overriden by calling it with a followlinks=True argument. 

# Deleting a single file 
# Method 1: Using os.remove() to delete files

import os
data_file '/Users/john/Desktop/Test/data.txt'

try:
  os.remove(data_file)
except PermissionError:
  print('Permission error: Unable to delete files')

# Method 2: Using os.unlink() to delete files

import os 
data_file '/Users/john/Desktop/Test/data.txt'
os.unlink(data_file)

# These two functions will throw an OSError if the path passed to them points to a directory instead of a file. To avoid this, you can either check that what you're trying to 
# delete is actually a file and only delete it if it is, or you can use exception handling to handle the OSError:

import os

data_file = '/home/data.txt'
if os.path.isfile(data_file):
  os.remove(data_file)
else:
  print(f'Error: {data_file} is not a valid filename')

# OR:

import os 
filename = "/etc/hosts"

if os.path.exists(filename) and os.path.isfile(filename):
	print("File exists")
else:
	print("File does not exist")


# The following example shows how to use exception handling to handle errors when deleting files:

import os

data_file = '/home/data.txt'
try:
  os.remove(data_file)
except OSError as e:
  print(f'Error: {data_file} : {e.strerror}')

# Method 3: Using pathlib.Path.unlink() to delete files

from pathlib import Path

data_file = Path('/home/data.txt')
try:
  data_file.unlink()
except IsADirectoryError as e:
  print(f'Error: {data_file} : {e.strerror}')

# Deleting a single directory or folder using os.rmdir() or pathlib.rmdir()
# NOTE: These two functions only work if the directory you're trying to delete is empty. If the directory isn't empty, an OSError is raised!

# Method 1: Using os.rmdir() to delete a directory 

import os
trash_dir = 'my_documents/bad_dir'

try:
  os.rmdir(trash_dir)
except OSError as e:
  print(f'Error: {trash_dir} : {e.strerror}') # if the directory isn’t empty, an error message is printed to the screen

# Method 2: Using pathlib to delete a directory

from pathlib import Path
trash_dir = 'my_documents/bad_dir'

try:
  trash_dir.rmdir()
except OSError as e:
  print(f'Error: {trash_dir} : {e.strerror}')

# Deleting entire directory trees and non-empty directories using shutil.rmtree()

import shutil
trash_dir = 'my_documents/bad_dir'

try:
  shutil.rmtree(trash_dir)
except OSError as e:
  print(f'Error: {trash_dir} : {e.strerror}') # everything in trash_dir is deleted when shutil.rmtree() is called on it

# OR:

os.removedirs("test1/test2") # removes every parent directory displayed in path until it encounters a non-empty directory

# There may be cases where you want to delete empty folders recursively. You can do this using one of the methods discussed above in conjunction with os.walk():

import os

for dirpath, dirnames, files in os.walk('.', topdown=False): # walks down the directory tree and tries to delete each directory it finds; if the directory isn't empty, an OSError is raised and that directory is skipped
  try:
    os.rmdir(dirpath)
  except OSError as ex:
    pass

# OR: you can perform a safedelete by using the third-party send2trash module after running $ pip install --user send2trash from a Terminal window to install it

import send2trash

baconfile = open('bacon.txt', 'a') # creates the file
baconfile.write('Bacon is not a vegetable')
baconfile.close()
send2trash.send2trash('bacon.txt')

# Copying files using shutil.copy() and shutil.copy2()
# NOTE: Using .copy2() preserves details about the file such as last access time, permission bits, last modification time and flags!!!!!!!

import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir' # or 'path/to/dest_dir/file1.txt' to move file.txt to the dest_dir directory under a different name
shutil.copy(src, dst) 

import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy2(src, dst)

# Copying an entire folder and every folder and file contained in it with shutil.copytree(source, destination). Calling it copies the folder at the path source, along with all
# of its files and subfolders, to the folder at the path destination. The soure and destination parameters are both strings.

shutil.copytree(p / 'SecLists', p / 'SecLists2') # creates a new folder named SecLists2 with the same content as the original SecLists folder; backup

# Moving files and directories using shutil.move(src, dst) (where src is the file or directory to be moved and dst is the destination)

import shutil

shutil.move('dir_1', 'backup/') # moves dir_1/ into backup/ if backup/ exists. If backup/ does not exist, dir_1 will be renamed to backup.

import os
import shutil 

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_audio(file):
  return os.path.splitext(file)[1] in audio

def is_video(file):
  return os.path.splitext(file)[1] in video

def is_image(file):
  return os.path.splitext(file)[1] in img

def is_screenshot(file):
  name, ext = os.path.splitext(file)
  return (ext in img) and "screenshot in name.lower()

os.chdir("/Users/patrick/Desktop")

for file in os.listdir():
  if is_audio(file):
    shutil.move(file, "/Users/patrick/Documents/audio")
  elif is_video(fiile):
    shutil.move(file, "/Users/patrick/Documents/video")
  elif is_image(file):
    if is_screenshot(file):
      shutil.move(file, "/Users/patrick/Documents/screenshots")
    else:
      shutil.move(file, "/Users/patrick/Documents/images")
  else:
      shutil.move(file, "/Users/patrick/Documents/")
    
# Renaming files and directories 

# Method 1: Using os.rename(src, dst)
# NOTE: if the destination path points to a directory, it will raise an OSError 

os.rename('first.zip', 'first_01.zip') 

# Method 2: Using rename() from the pathlib module

from pathlib import Path

data_file = Path('data_01.txt') # first, you need to create a pathlib.Path() object that contains a path to the file you want to replace
data_file.rename('data.txt')
