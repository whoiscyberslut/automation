# Change file ownership in Linux 

# Example 1: Using shutil.chown() method 

from shutil import chown 

# You can use username or uid 
# Must provide at least one of user/group, or both
chown('test.txt', user='nanodano')
chown('test.txt', group='sudo')
chown('test.txt', user=0, group=0) # root uids 
chown('test.txt', user='root', group='root')

# Example 

from shutil import chown

def change_file_ownership(filename, user, group):
    try:
        chown(filename, user=user, group=group)
        print(f"Changed ownership of {filename} to user: {user}, group: {group}")
    except Exception as e:
        print(f"Error changing ownership of {filename}: {e}")

# Example usage
filename = 'test.txt'
user = 'root'
group = 'root'

change_file_ownership(filename, user, group)

# OR: 

import shutil
import getpass

shutil.chown('my.txt', user=getpass.getuser())

# Method 2: Using shutil.chown() method in a function 

import shutil
from pathlib import Path

def change(path, uid, gid):
  try:
    info = Path(path)
    user = info.owner()
    group = info.group()
    print("Present owner and group")
    print("Present owner:", user)
    print("Present group:", group)
    shutil.chown(path, uid, gid)
    print("\n The owner and the group have been changed successfully")
    info = Path(path)
    user = info.owner()
    group = info.group()
    print("Present owner now:", user)
    print("Present group now:", group)
  except FileNotFoundError:
    print("File not found:", path)
  except Exception as e:
    print("An error occurred:", e)

# Example usage
# path = "/root/trial.py"
# uid = 10
# gid = 10
# change(path, uid,. gid)

# Example 2: Using the os.chown() method to change the owner and group ID of the given path to the specified numeric owner ID (UID) and group (GID). 
# The script prints the current owner and group IDs, changes them to the provided uid and gid, and then displays the updated IDs.

import os

def change(path, uid, gid):
  try:
    print("File's owner ID:", os.stat(path).st_uid)
    print("File's group ID:", os.stat(path).st_gid)
    os.chown(path, uid, gid)
    print("\n Owner ID and group ID of the file have been changed successfully")
    print("\n File's owner ID now is:", os.stat(path).st_uid)
    print("File's group ID now is:", os.stat(path).st_gid)
  except FileNotFoundError:
    print("File not found:", path)
  except Exception as e:
    print("An error occurred:", e)

# Example usage: 
# path = "/root/trial.py"
# uid = 1500
# gid = 1500
# change(path, uid, gid)

# Method 2: Changing owner ID only while maintaining the existing group ID

import os

def change_owner(path, uid):
  try:
    print("File's owner ID:", os.stat(path).st_uid)
    print("File's group ID:", os.stat(path).st_gid)
  gid = -1
  os.chown(path, uid, gid)
  print("\n Owner ID of the file has been changed successfully, leaving the group ID unchanged")
  print("\n File's owner ID now is:", os.stat(path).st_uid)
  print("File's group ID now is:", os.stat(path).st_gid)
except FileNotFoundError:
  print("File not found:", path)
except Exception as e:
  print("An error occurred", e)

# Example usage:
# path = "/root/trial.py"
# uid = 200
# change_owner(path, uid)
