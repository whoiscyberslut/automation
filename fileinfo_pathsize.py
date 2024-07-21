import os

def extract_info(path='.'):
    dict_list = []  # List to store file information

    for root, dirs, files in os.walk(path):  # Recursively iterate over all files/directories in the path directory
        for file_name in files:
            file_dict = {}
            file_path = os.path.join(root, file_name)
            file_dict['path'] = file_path  # Get the path name of the file
            file_dict['size'] = os.path.getsize(file_path)  # Get the file size
            dict_list.append(file_dict)  # Append file info dictionary to the list
    
    return dict_list  # Return the list

# # Example usage

if __name__ == "__main__":
    directory_path = "/example_directory"  # Specify the directory you want to scan
    file_info_list = extract_info(directory_path)

    for file_info in file_info_list:
        print(f"File Path: {file_info['path']}, Size: {file_info['size']} bytes")

