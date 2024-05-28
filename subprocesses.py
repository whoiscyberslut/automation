'''
Using the subprocess module in Python

 subprocess.run() is a convenient way to run a subprocess and wait for it to complete. It lets you choose the command to run and add options like arguments, env variables, and input/output redirections. Once the 
 subprocess is started, the run() method blocks until the subprocess completes and returns a CompletedProcess object, which contains the return code and output of the subprocess (stout and stderr as bytes objects). 
 It takes several arguments:
 
 (1) args: The command to run and its arguments, passed as a list of strings 
 (2) capture_output: When set to True, it will capture the standard output and standard error.
 (3) text: When set to True, it will return the stdout and stderr as string, otherwise it will return them as bytes.
 (4) check: A Boolean value that indicates whether to check the return code of the subprocess, if check=True and the return-code is non-zero, then subprocess CalledProcessError is raised
 (5) timeout: A value in seconds that specifies how long to wait for the subprocess to complete before timing out 
 (6) shell: A Boolean value that indicates whether to run the command in a shell. This means that the command is passed as a string, and also shell-specific features can be used (e.g. wildcard expansion and variable substitution)
'''

import subprocess

result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(result.stdout)

# Example 1: Running Python scripts using the subprocess.run() method

import subprocess
result = subprocess.run(["python3", "my_python_file.py"], capture_output=True, text=True)
print(result.stdout) 

# OR: running Python code directly from a function 

result = subprocess.run(["C:\Users\owner\anaconda3\python", "-c", "print('This is directly from a subprocess.run() function')"], capture_output=True, text=True)
print(result.stdout)

# Output: This is directly from a subprocess.run() function

# Using the check argument - a Boolean value that controls whether the function should check the return code of the command being run - when check is set to True, the function will check the return code of the
# command and raise a CalledProcessError exception if the return code is non-zero (the exception will have the return code, stdout, stderr, and command as attributes). When check is set to False (default), 
# the function will not check the return code and will not raise an exception, even if the command fails.

import subprocess

result = subprocess.run(["python", "file_donot_exist.py",], capture_output=True, text=True, check=True)
print(result.stdout)
print(result.stderr)

# Output: CalledProcessError: Command '['python', 'file_donot_exist.py']' returned non-zero exit status 2.

# BUT: if you set check=True, your process won't fail; instead, you will get the error message in stdout 

import subprocess

result = subprocess.run(["python", "file_donot_exist.py",], capture_output=True, text=True, check=False) 

# Output: python: can't open file 'my_python_file2.py': [Errno 2] No such file or directory

# Example 2: Using the subprocess.run() function to execute the date command, capture the output and remove trailing newline(s?)

import subprocess 

f = subprocess.run)["date"], capture_output=True, text=True).stdout.rstrip("\n") # the capture_output=True argument allows the command's output to be captured
print('Date is:', f)

# Example 3: Using the mkdir command in the run method to create new directories from the contents of a directories.txt file

import subprocess

with open("directories.txt", "r") as directories:
  for dirs in directories:
    subprocess.run("mkdir ./{0}".format(dirs), shell=True, capture_output=True)

subprocess.run("ls", shell=True) # to verify that the script created all the directories

# Example 2: Using Python subprocess.popen()

# Capture the output of the date command

f = os.Popen("date").read()
print(f) # returns the current date, which is stored in the variable f and then printed

# The popen class has several methods that allow you to interact with the process, such as communicate(), poll(), wait(), terminate(), and kill().

import subprocess

p = subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) # runs the command python --help and creates a new Popen object, which is stored in the variable p
output, errors = p.communite() # captures the standard output and error of the command 
print(output) 

# Python subprocess pipe: Python subprocess module provides a way to create and interact with child processes, which can be used to run other programs or commands. One of the features of the subprocess module
# is the ability to create pipes, which allow communication between the parent and child processes. Pipes can be created using the subprocess module with the Popen class by specifying the stdout or stdin 
# argument as subprocess.PIPE
# Example: the following code creates a pipe that connects the output of the ls command to the input of the grep command, which filters the output to show only the lines that contain the word "file":

import subprocess

ls_process = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
grep_process = subprocess.Popen(["grep", "sample", stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)
output, error = grep_process.communicate()
print(output)
print(error)

# OR:

import subprocess

try:
  result = subprocess.run(['ls'], stdout=subprocess.PIPE, text=True, check=True)
  print("Output of the command: ")
  print(result.stdout)
except subprocess.CalledProcessError as e:
  print(f"Command execution failed with error code {e.returncode}:)
  print(e.stderr)

# Output: sample data

program = "mediaplayer.exe"
process = subprocess.Popen(program)
code = process.wait()
print(code)

# Output: 0

# Starting a process using the Popen function call by passing 2 parameters in the function call: (1) the program you want to start, and (2) the file argument 

from subprocess import Popen, PIPE

process = Popen(['cat', 'example.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)

# Output: ... Program finished with exit code 0 \n Press ENTER to exit console.

# Example 3: Using the call() - a function that is used to run a command in a separate process and wait for it to complete. It returns the return code of the command, which is zero, if the command
# was successful, and non-zero, if it failed. The command is useful whenyou want to run a command and check the return code, but do not need to capture the output. The call() function takes the same arguments as run(). 

import subprocess

return_code = subprocess.call(["python", "--version"]) # runs the command python --version in a separate process and waits for it to complete; the command's return code will be stored in this variable

if return_code == 0:
  print("Command executed successfully.")
else:
  print("Command failed with return code:", return_code)

# Example: calling a subprocess for the built-in Unix command "ls -l"

import subprocess

subprocess.call(["ls", "-l"])

# Output:
'''
total 4
-rw-r--r-- 1 14093 14093 48 Apr 7 06:32 main.py

...Program finished with exit code 0
Press ENTER to exit console. 
'''

# Define command and options wanted

command = "head -n 1"
filename = input("Please introduce name of the file of interest:\n")
return_value = subprocess.call(command + filename, shell=True)
print('##############')
print('Return value:', return value)

# A preferrable way to run subprocess.call is by using shell=False (it is the default option, so no need to specify it). Then we can simply call subprocess.call(args), 
# where args[0] contains the command, and args[1:] contains all the extra options to the command. 

# If you are putting shell=False, you need to specify your command in the form of a list, e.g. command = ["ls", "-l"]; if you are putting shell=True, you can put your 
# command in the form of a string, like so: 

command = "ls -l"
rt = sp.wait()
out, err = sp.communicate()
print(out)
print(err)

# Example where we would use shell = True:

import subprocess

command = ["echo", "$SHELL"]
sp = subprocess.Popen(command, shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
rt = sp.wait()
out, err = sp.communicate()
print(out)
print(err)

# If shell = False: we are literally getting the value back (i.e. echo $SHELL); when shell = True, you are going to execute your command literally, so you need 
# to enclose it in double quotes, like so:

command = "echo $SHELL" # -> /bin/zsh

# Example 

import subprocess

command = "head"
options = "-n 1"

filename = input("Please introduce name(s) of file(s) of interest:\n") # Now it's safe from shell injection

# Create list with arguments for subprocess.call
args = []
args.append(command)
args.append(options)
for i in filename.split():
 args.append(i)

# Run subprocess.call and save return_value
return_value = subprocess.call(args)
print('############')
print('Return value:', return_value)

# Example 4: Using check_output() - a function that is similar to run(), but it only returns the standard output of the command, and raises a CalledProcessError exception if the return code is non-zero. It takes the 
# same arguments as run(). It also returns the standard output of the command as a bytes object or string, if text=True is passed. Additionally, it can be passed an universal_newlines Boolean parameter.

import subprocess

try:
  output = subprocess.check_output(["python", "--version"], text=True)
  print(output)
except subprocess.CalledProcessError as e:
  print(f"Command failed with return code {e.returncode}")

# Example output: `Python 3.8.8`

# Using universal_newlines=True returns the output as a string instead of bytes

import subprocess

output = subprocess.check_output('ls', universal_newlines=True)
print(output)

# Output:

'''
file1
file2
dir1
'''

# Using subprocess.CalledProcessError in the except clause to deal with the error in a controller manner and get information about it

import subprocess

command = "head"
options = "-n 1"

filename = input("Please introduce name(s) of file(s) of interest:\n")
# Create list with arguments for subprocess.check_output
args = [] 
args.append(command)
args.append(options)
for i in filename.split():
 args.append(i)
 # Run subprocess.check_output and save command output
try:
 output = subprocess.check_output(args)
 # Use decode function to convert to a string
print('###########')
print('Output: ', output.decode("utf-8"))
# If checks_output returns an error:
except subprocess.CalledProcessError as error:
 print('Error code: ', error.returncode. '.Output', error.output.decode("utf-8"))

