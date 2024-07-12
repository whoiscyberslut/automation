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

# OR: filter processes by specific user

import psutil

# Specify the user to filter processes by
specific_user = "john"  # Replace "john" with the desired username

# Get process information
processes = psutil.process_iter(['pid', 'name', 'username'])
print(f"Running processes for user '{specific_user}':")
for process in processes:
    if process.info['username'] == specific_user:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}")

# OR: Find the length of all running PIDs

import psutil

pids = psutil.pids()

# Calculate the number of running processes
num_pids = len(pids)

# Print the number of running processes
print("Number of running processes:", num_pids)

# OR: 

import psutil

processes = psutil.process_iter()

for process in processes:
    print(f"Process ID: {process.pid}, Name: {process.name()}")

# import psutil
# [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['name']]

# A script that passes a script (file name) to the user defined function is_process_running(), returning True or False.

import psutil

def is_process_running(name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return True
    return False
if is_process_running('script.py'):
    print('The script is running.')
else:
    print('The script is not running.')

# Check whether a script is running on Linux: 

import subprocess

script_name = "sample.py"
ps_output = subprocess.check_output(["ps", "-ef"])
ps_lines = ps_output.decode("utf-8").split("\n")
for line in ps_lines:
    if script_name in line:
        print("The script is running")
        break
else:
    print("The script is not running")
  
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

# OR: 

import subprocess

def ping(host):
    cmd = 'ping'
    # Send two packets of data to the host; this is specified by '-c 2' in the args list 
    temp = subprocess.Popen([cmd, '-c 2', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  
    # Get the output of ping 
    output, error = temp.communicate()
    
    if error:
        print(f"Error: {error.decode()}")
        return
    
    output = output.decode()  # Decode the byte output to string
    
    # Split the output into lines
    output_lines = output.split("\n")
  
    # Print the results
    print('Ping results:')
    for line in output_lines:
        print(line)

    return output_lines

if __name__ == '__main__':
    ping('www.google.com')

#import subprocess 
#import os 
  
# A function to ping given host 
#def ping(host): 
#    cmd = 'ping'
#    # Send two packets of data to the host;this is specified by '-c 2' in the args list 
#    temp = subprocess.Popen([cmd, '-c 2', host], stdout = subprocess.PIPE) 
  
    # Get the output of ping 
#    output = str(temp.communicate()) 
#    output = output.split("\n") 
#    output = output[0].split('\\') 
#    # A variable to store the result:
#    res = [] 
  
#    for line in output: 
#        res.append(line) 
  
    # Print the results: 
#    print('Ping results: ') 
#    print('\n'.join(res[len(res) - 3:len(res) - 1])) 
  
#    return res 
  
#if __name__ == '__main__': 
#  ping('www.google.com') 

# OR: 

def ping(mysite):
    myping = ("ping -q -c 1 %s > /dev/null" % mysite)
    status = os.system(myping)
    return(status)

with open("sites.txt") as file:
    mysites = file.readlines()

for site in mysites:
    mystatus = ping(site.strip())
    if mystatus == 0:
   	 print(site.strip() + " is fine")
    if mystatus != 0:
   	 print("********************")
   	 print("vvvvvvvvvvvvvvvvvvvv")
   	 print("%s is down!" % (site.strip()))
   	 print("^^^^^^^^^^^^^^^^^^^^")
   	 print("********************")
    print("-----------")


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
