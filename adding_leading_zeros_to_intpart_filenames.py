# Example: there are files generated, where the filename contains within itself an integer, but also has a prefix like so:
# e.g. snapshot_data_vss_10000.caffemodel, snapshot_data_vss_iter_1000.caffemodel, snapshot_data_vss_iter_500.caffemodel and so on. 
# Use case: pad the integers with leading zeros

# Solution 1: Using formatted strings
filenames = ['snapshot_data_vss_10000.caffemodel', 'snapshot_data_vss_iter_1000.caffemodel', 'snapshot_data_vss_iter_500.caffemodel']

iters = 500
for file in filenames:
    print(f'snapshot_data_vss_iter_{iters:03}.caffemodel')
    iters += 500

# OR

import os
import re

def pad_filenames_with_zeros(directory):
    # Define a regex pattern to match the filenames and extract the integer part
    pattern = re.compile(r"(snapshot_data_vss(?:_iter)?)_(\d+)(\.caffemodel)")

    # List all files in the given directory
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            prefix = match.group(1)
            number = match.group(2)
            suffix = match.group(3)
            
            # Pad the integer part with leading zeros (up to 5 digits for this example)
            new_number = f"{int(number):05}"
            new_filename = f"{prefix}_{new_number}{suffix}"
            
            # Construct the full paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Directory containing the files
directory = '/path/to/your/folder'

# Call the function to pad filenames with zeros
pad_filenames_with_zeros(directory)

# Usage: 

# snapshot_data_vss_1.caffemodel
# snapshot_data_vss_10.caffemodel
# snapshot_data_vss_100.caffemodel
# snapshot_data_vss_iter_5.caffemodel
# snapshot_data_vss_iter_50.caffemodel

# TO: 

# snapshot_data_vss_00001.caffemodel
# snapshot_data_vss_00010.caffemodel
# snapshot_data_vss_00100.caffemodel
# snapshot_data_vss_iter_00005.caffemodel
# snapshot_data_vss_iter_00050.caffemodel

# OR: 

import os
import re

def pad_filenames_with_zeros_and_increment(directory):
    # Define a regex pattern to match the filenames and extract the integer part
    pattern = re.compile(r"(snapshot_data_vss(?:_iter)?)_(\d+)(\.caffemodel)")

    # List all files in the given directory and filter based on the regex pattern
    filenames = [filename for filename in os.listdir(directory) if pattern.match(filename)]

    # Sort filenames based on the number extracted by the regex pattern
    filenames.sort(key=lambda x: int(pattern.match(x).group(2)))

    # Initialize the iteration counter
    iters = 500

    for filename in filenames:
        match = pattern.match(filename)
        if match:
            prefix = match.group(1)
            suffix = match.group(3)

            # Pad the iteration number with leading zeros (up to 3 digits)
            new_number = f"{iters:03}"
            new_filename = f"{prefix}_iter_{new_number}{suffix}"

            # Construct the full paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

            # Increment the iteration counter
            iters += 500

# Directory containing the files
directory = '/path/to/your/folder'

# Call the function to pad filenames with zeros and increment the iteration number
pad_filenames_with_zeros_and_increment(directory)

# OR: 

import re

# Define the regex pattern
pattern = re.compile(r"(snapshot_data_vss(?:_iter)?)_(\d+)(\.caffemodel)")

# Function to extract the numeric part from a filename
def extract_numeric_part(filename):
    match = pattern.match(filename)
    if match:
        return int(match.group(2))
    else:
        return 0  # Return 0 if no match found (you can adjust this as needed)

# Example list of filenames
filenames = ['snapshot_data_vss_100.caffemodel', 'snapshot_data_vss_10.caffemodel', 'snapshot_data_vss_50.caffemodel']

# Sort filenames based on the numeric part extracted using the function
sorted_filenames = sorted(filenames, key=extract_numeric_part)

print(sorted_filenames)
