# This script is original work of @deoluoyinlola. It will be used for personal purposes and removed from the repo afterwards.

import os

dict_list = []

def extract_info(path = '.'): #function to extract file info, defaulted to present working directory if path is not passed
    dict_list = []

    for root, dirs, files in os.walk(path): #recursively iterate over all files/directiories in path directory
        for file_name in files:
            file_dict = {}
            file_dict['path'] = os.path.join(root, file_name) #get path name of file
            file_dict['size'] = os.path.getsize(os.path.join(root, file_name)) #get file size
            dict_list.append(file_dict) #appends file info dictionary to the list
    
    return dict_list #returns list

# OR:

import os

dict_list = []

for file in os.listdir(): #loop through all the files in current path
    file_dict = {}
    file_dict['path'] = os.path.realpath(file) #get path name of file
    file_dict['size'] = os.path.getsize(file) #get size of file
    dict_list.append(file_dict) #add dictionary of file information to list

print(*dict_list, sep="\n") #print each dictionary of file information in new line

# This script uses os.listdir() to list all files in the current directory (os.listdir() lists only the files and directories in the 
# specified directory but does not recurse into subdirectories).
