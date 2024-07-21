import os
import subprocess

def list_files(directory='.'):
    # Use subprocess.run to execute the 'ls' command and capture output
    result = subprocess.run(['ls', '-l', directory], capture_output=True, text=True)
    # Split the output into lines
    output_lines = result.stdout.splitlines()
    return output_lines

def get_permissions(directory='.'):
    output_lines = list_files(directory)
    
    permissions = {}
    
    # Process each line of the output
    for line in output_lines[1:]:  # Skip the first line (total line)
        parts = line.split()
        if len(parts) >= 9:  # Ensure there are enough parts to extract info
            permission_value = parts[0]
            folder_name = parts[-1]
            permissions[folder_name] = permission_value
    
    # Ensure 'outputs' directory exists
    os.makedirs('outputs', exist_ok=True)
    
    # Write the permissions to 'permissions.txt'
    with open(os.path.join('outputs', 'permissions.txt'), 'w') as out_file:
        out_file.write('Folder Name   Permissions\n\n')
        for folder, perm in permissions.items():
            out_file.write(f"{folder} : {perm}\n")

    return permissions

if __name__ == '__main__':
    get_permissions()
