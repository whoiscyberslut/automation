import subprocess 
import os 
  
# A function to list the files in the current directory and  parse the output. 

def list_command(args = '-l'): 
    cmd = 'ls'
    # Using the Popen function to execute the command and store the result in temp. It returns a tuple that contains the  
    # data and the error if any. 
    temp = subprocess.Popen([cmd, args], stdout = subprocess.PIPE) 
    # We use the communicate function to fetch the output.
    output = str(temp.communicate()) 
    # Splitting the output so that we can parse them line by line.
    output = output.split("\n") 
# ?    output = output[0].split('\\') 

    # A variable to store the output:
    res = [] 

    # Iterate through the output line by line:
    for line in output: 
        res.append(line) 
  
    # Print the output:
    for i in range(1, len(res) - 1): 
        print(res[i]) 
  
    return res 
  
# Parse the output of the "ls" command and fetch the permissions of the files and store them in a text file.

def get_permissions(): 
    # Get the output of the ls command:
    res = list_command('-l') 
  
    permissions = {} 
      
    # Iterate through all the rows and retrieve the name of the file and its permission:
    for i in range(1, len(res) - 1): 
        line = res[i] 
        line = line.split(' ') 
        folder_name = line[len(line) - 1] 
        permission_value = line[0] 
        permissions[folder_name] = permission_value 
  
    # Create a directory called "outputs" to store the output files:
    try: 
        os.mkdir('outputs') 
    except: 
        pass
    os.chdir('outputs') 
  
    # Open the output file: 
    out = open('permissions.txt', 'w') 
    out.write('Folder Name   Permissions\n\n') 
  
    # Write to the output file: 
    for folder in permissions: 
        out.write(folder + ' : ' + permissions[folder] + '\n') 

    os.chdir('..') 
    return permissions 
  
if __name__ == '__main__': 
    list_command('-al') 
