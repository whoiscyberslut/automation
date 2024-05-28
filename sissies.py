# With the help of the sys module, arguments can be passed to the Python scripts

import sys 

print('\n')
print('The name of the script is: %s' %sys.argv[0]) # name of the script
print('The input to the script is: %s' %sys.argv[1]) # argument passed by user

# Example 1: Get the OS name by using the sys module

import sys
sys.platform # returns 'linux' 

# OR: use the uname function of the os module to get a detailed description about the current operating system, such as the name, machine, release details, version, and 
# hardware configuration.

import os
os.uname()

# Output: posix.uname_result(sysname='Linux', nodename='kali', release='5.6.0-2-kali2-amd64', version='#1 SMP Debian 5.6.14-2kali1 (2020-06-10)', machine='x86_64)

# Example 2: Get the Python version

import sys
print(sys.version)

# Example 3: Get the platform using the sys module

import sys
print(sys.platform) # => 'Linux'

# Example 4: Get the path using the sys module

import sys
print(sys.path)

# Example 5: Get the modules that Python is imporing using the sys module

import sys
sys.modules

# Example 6: Using sys.exit()

if not path.exists("/etc/xxx"):
  sys.exit()

# OR:

if len(sys.arv) != 3:
  print("This script needs at least 3 command-line arguments")
  sys.exit()
