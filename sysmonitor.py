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
os.getlogin() 

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

# Example 8: Getting the UID and GID of a system using the os module

os.getuid() # -> 1000
os.getgid() # -> 1000

