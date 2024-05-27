# Checking permissions of a file 

import os

stats = os.stat('test.txt')
print(stats.st_mode)
print(oct(stats.st_mode)) # Octal output, e.g. 0o777, 0o644

# Setting file permissions (chmod)

import stat

stat.S_IRUSR # Read, user 
stat.S_IWUSR # Write, user 
stat.S_IXUSR # Execute, user 

stat.S_IRGRP # Read, group
stat.S_IWGRP # Write, group
stat.S_IXGRP # Execute, group

stat.S_IROTH # Read, other 
stat.S_IWOTH # Write, other
stat.S_IXOTH # Execute, other

stat.S_IRWXU # Read, write, and execute for user
stat.S_IRWXG # Read, write, and execute for group 
stat.S_IRWXO # Read, write, and execute for other

# For example, to set all permissions for user only, you would do so bitwise OR set all the user permissions like this: S_IRUSR|S_IWUSR|I_XUSR.
# The example below shows how to grant all permissions, the equivalent to chmod 777.

import os
import stat 

# Equivalent to chmod 777 
os.chmod('test.txt', stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)

# Method 2: Using os.chmod to set the permissions bitwise 

import os
import sys

os.chmod('myfile.txt', 0o644)
os.chmod('mydir', 0o755)
os.chmod('test', 774)

# Check file permissions for the current user (including any additional permissions granted through group membership or other means (like ACLs))

import os 

def check_file_permissions(file_path):
  if os.access(file_path, os.R_OK):
    print(f"Read permission is granted for file: {file_path}")
  else:
    print(f"Read permission is not granted for file: {file_path}")
  if os.access(file_path, os.W_OK):
    print(f"Write permission is granted for file: {file_path}")
  else:
    print(f"Write permission is not granted for file: {file_path}")
  if os.access(file_path, os.X_OK):
    print(f"Execute permission is granted for file: {file_path}")
  else:
    print(f"Execute permission is not granted for file: {file_path}")

# Example usage: check_file_permissions(file_path)

# Method 2: Making use of the os.path module and checking whether the given path exists and whether the file is non-empty

import os 

def check_file_permissions(file_path):
  if os.path.isfile(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
      print(f"File exists and is not empty: {file_path}")
      if os.access(file_path, os.R_OK):
        print(f"Read permission is granted for file: {file_path}")
      else:
        print(f"Read permission is not granted for file: {file_path}")
    else:
      print(f"File does not exist or is empty: {file_path}")
  else:
    print(f"Path does not point to a file: {file_path}")

# Example usage: check_file_permissions(file_path)

# Method 3: Making use of the pathlib module 

import os
from pathlib import Path

def check_file_permissions(file_path):
  file = Path(file_path)
  if file.is_file():
    if os.access(file_path, os.R_OK):
      print(f"Read permission is granted for file: {file_path}")
    else:
      print(f"Read permission is not granted for file: {file_path}")
    if os.access(file_path, os.W_OK):
      print(f"Write permission is granted for file: {file_path}")
    else:
      print(f"Write permission is not granted for file: {file_path}")
    if os.access(file_path, os.X_OK):
      print(f"Execute permission is granted for file: {file_path}")
    else:
      print(f"Execute permission is not granted for file: {file_path}")
  else:
    print(f"The specified does not point to a file: {file_path}")

# Example usage: check_file_permissions("/path/to/file.txt")

# Example 2: Check for file permissions for the owner of a file as recorded in the file's metadata

# Context: These checks are specific to the file's owner permissions, as stored in the file's metadata. It doesn't account for the current user's effective permissions unless 
# the current user is the file's owner. This reflects what permissions are set for the owner of the file, regardless of the actual user running the script.

import os
import stat

def check_file_permissions(file_path):
  file_stat = os.stat(file_path)
  file_mode = file_stat.st_mode
  if stat.S_IRUSR & file_mode:
    print(f"Read permission is granted for the owner of file: {file_path}")
  else:
    print(f"Read permission is not granted for the owner of file: {file_path}")
  if stat.S_IWUSR & file_mode: 
    print(f"Write permission is granted for the owner of file: {file_path}")
  else:
    print(f"Write permission is not granted for the owner of file: {file_path}")
  if stat.S_IXUSR & file_mode:
    print(f"Execute permission is granted for the owner of file: {file_path}")
  else:
    print(f"Execute permission is not granted for the owner of file: {file_path}")

# Example usage: check_file_permissions(file_path)

# Example 3: Change file permissions using the subprocess module (NOT TESTED!)

import subprocess
subprocess.call(['chmod', '0444', 'myfile.txt'])


