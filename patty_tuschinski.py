from pathlib import Path
import os 

Path('spam', 'bacon', 'eggs')
str(Path('spam', 'bacon', 'eggs'))
print(os.getcwd())
Path.cwd() # Output: /home/user
Path.cwd().parents[0] # Output: /home
Path.cwd().parents[1] # Output: /
Path.home()
os.chdir('/path/to/directory')
myfiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myfiles:
  print(Path(r'/home/user', filename))
print(Path('spam') / 'bacon' / 'eggs')  
print(Path('spam') / Path('bacon/eggs'))  
print(Path('spam') / Path('bacon', 'eggs')) # NOTE: either the first or the second leftmost value must be a Path object for the entire expression to evaluate to a Path object!!

homefolder = Path('/home/user')  
subfolder = Path('spam')  
print(homefolder / subfolder )  
print(str(homefolder / subfolder))

Path.cwd().is_absolute() # returns True or False
Path('/path/to/directory').is_absolute()

# To get an absolute path from a relative path, you can put Path.cwd() / in front of the relative Path object

# OR: Use os.path module's functions related to absolute and relative paths:
# (1): Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one
# (2): Calling os.path.isabs(path) will return True if the argument is an absolute path and False is it is a relative path
# (3):  Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used.

# Checking path validity with p.exists(), p.is_file(), and p.is_dir()

print(p.exists())  # returns True or False
ddrive = Path('E:\')
print(ddrive.exists()) # checks for a flash drive with the volume named D:\
              
print(p.is_file()) # returns True or False
print(p.is_dir()) # returns True or False
              
# OR: use the older os.path module to accomplish the same task with the os.path.exists(path), os.path.isfile(), and os.path.isdir(path) functions)

filename = Path("source_data/text_files/raw_data.txt")

print(filename.name) # prints "raw_data.txt"
print(filename.suffix) # prints "txt"
print(filename.stem) # prints "raw_data"

if not filename.exists():
  print("Oops, file doesn't exist!")
else:
  print("Yay, the file exists!")

# Use pathlib to generate file:// urls and open a local file in your web browser

import webbrowser
from pathlib import Path
filename = Path("source_data/text_files/raw_data.txt")
webbrowser.open(filename.absolute().as_uri())

# Using Path() to get a string with a file path using the correct 
