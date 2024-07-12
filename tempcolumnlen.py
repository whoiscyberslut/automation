# Example file content: 

# Step Temp Enthalpy
# 0    0    -368
# 100  1    -369
# 200  2    -372
# 300  6    -362
# 400  9    -365

import os

def parse_file_and_get_temp_length(file_path):
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        
        # Initialize an empty list to store the Temp values
        temp_values = []
        
        # Read the file line by line
        for line in file:
            # Split the line into columns
            columns = line.split()
            
            # Extract the Temp value (second column)
            temp = columns[1]
            
            # Add the Temp value to the list
            temp_values.append(temp)
        
    # Print the length of the Temp values list
    print("Length of Temp values:", len(temp_values))

# Replace 'your_file.txt' with the path to your actual file
parse_file_and_get_temp_length('your_file.txt')
