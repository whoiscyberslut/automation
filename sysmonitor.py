# Example 1: Using Python's psutil library to access information about CPU usage, memory consumption, disk usage, and network statistics.

import psutil 

# Get CPU information 
cpu_percent = psutil.cpu_percent() 
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()

# Get memory information 
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
# Print memory usage %
print(f"Memory usage: {virtual_memory.percent}")

# Get disk usage information
disk_usage = psutil.disk_usage('/')
# Print disk usage %
print(f"Disk usage: {disk_usage.percent}")

# Get network information
net_io = psutil.net_io_counters()

# Get process information
proceses = psutil.process_iter(['pid', 'name', 'username'])
print("Running processes: ")
for process in processes:
  print(f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}")

# Example 2: Getting the name of the current user logged in the system using the os module

import os
try:
  user = os.getlogin() 
  print(user)
except:
  print("An error occurred")

# Output: 'rashan'

# Example 3: Getting the size of the terminal using the os module

import os
os.get_terminal_size()

# Output: os.terminal_size(columns=80, lines=24) 

# To get individual columns' or lines' size:

import os

col, lines = os.get_terminal_size()
print("Number of columns: ", col)
print("Number of lines: ", lines)

# Example 4: Retrieving the current process ID using os.getpid(), and the parent process ID using os.getppid()

import os

print(os.getpid()) # Get the current process ID; returns 12345
print(os.getppid()) # Get the parent process ID; returns 12344

# Example 5: Retrieving environment variales with os.getenv()

import os
print(os.environ['HOME']) # gets the value of the 'HOME' environmental variable

# Setting Up environment variables and shell context

import subprocess
import os

# Create a copy of the current environment variables
env_vars = os.environ.copy()
# Add/Modify an environment variable
env_vars["MY_VARIABLE"] = "MyValue"
subprocess.run(['printenv', 'MY_VARIABLE'], env=env_vars)

# Example 6: Using the os.name() function to return the name of the operating system familly, as specified by the IEEE

import os
import time

print(os.name)

# Example 7: Executing shell commands using os.system() - first we install the os-sys library by running $ pip install os-sys in the Terminal window

os.system('echo "Hello World!')
os.system("cls" if os.name == "nt" else "clear")
print("Cleared the terminal screen")
x = os.system(ls -lah)
print(0) # -> 0; one of the major drawbacks of the os module is that it doesn't store the output of your command, it only stores the exit code -> use subprocess module
os.system(ps aux | grep firefox) # if you have Firefox running, the command will find the process and print out information on it
os.system('df -h')
host_to_ping = 'google.com'
os.system(f'ping -c 4 {host_to_ping}')

command = "head -n 1"

filename = input("Please introduce name of file of interest:\n")
return_value = os.system(command + " " + filename)

print('##############')
print('Return Value:', return_value)

# Handling errors:

import os 
home_dir = os.system("cd ~") 
print("`cd ~` ran with exit code %d" % home_dir) 
unknown_dir = os.system("cd doesnotexist") 
print("`cd doesnotexis` ran with exit code %d" % unknown_dir)

# Example output:

'''
$ python3 cd_return_codes.py
`cd ~` ran with exit code 0
sh: line 0: cd: doesnotexist: No such file or directory
`cd doesnotexist` ran with exit code 256
'''

# Example 8: Getting the UID and GID of a system using the os module

os.getuid() # -> 1000
os.getgid() # -> 1000

# Example 7: Creating a Python wrapper around the ping command that only prints wheher the host is reachable or not

import subprocess

def simple_ping(host):
  result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if result.returncode == 0:
    print(f"{host} is reachable.")
  else:
    print(f{host} is not reachable.")

  host = input("Enter a host to ping: ")
  simple_ping(host)

# Example 8: Fetching the free disk space

import subprocess

def get_free_space():
  result = subprocess.run(['df', '-h'].stdout.subprocess.PIPE)
  print(result.stdout,decode())

get_free_space()

# Example 8: Backing up a directory regularly

import subprocess

def backup_directory(src, dest):
# Check if the source directory exists
  if not os.path.isdir(src):
    print(f"Source directory {src} does not exist.")
    return
    
  try:
  # Creating a tarball of the source directory
    subprocess.run(['tar', '-czf', dest, src])
    print(f"Backup of {src} created at {dest}")
  except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the backup: {e}")

src_dir = '/path/to/source/dir'
backup_path = '/path/to/backup.tar.gz'

# Ensure paths are absolute
src_dir = os.path.abspath(src_dir)
backup_path = os.path.abspath(backup_path)

backup_directory(src_dir, backup_path)

# Example 9: Using the platform module to find out what OS is running

import platform

platform.uname()
platform.system() # similar to uname command

if platform.system() == 'Linux':
  os.system('ls')
elif platform.system() == 'Windows':
  os.system('dir')
else:
  print('Unsupported operating system')

# Output: 'Linux'

# Example 9: Using the platform module to find out the architecture

import platform

platform.architecture() # => ('64bit', 'ELF')
platform.machine() # if you dont want output in the form of this tuple; => 'x86_64'

# Example 9: Using the platform module to find out the specific kernel version of the OS

import platform

platform.release() # => '5.8.0-55-generic' 

# Example 9: Using the platform module to find out the Python version

import platform

platform.python_version() # => '3.8.5'
platform.python_version_tuple() # => ('3', '8', '5')

# Example 10: Using Pyhon's getpass module

import getpass

password = input("Please enter your password: ")
my_pass = getpass.getpass()  
# print("Entered password is: ", my_pass)

# OR:

print("Please enter your password: ")  
my_pass = getpass.getpass(prompt = "Enter your password: ") 

getpass.getuser()
