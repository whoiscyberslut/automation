# Example file (input.txt):

# -3153.61743,-6115.18164,-3289.31226
# -3256.75195,-6075.70801,-3550.83057
# -3775.00977,-5870.36035,-3817.91870
# -3890.03223,-5819.92871,-3797.58984
# -4134.60156,-5724.16309,-3651.39648

first_column = []

with open('input_text.txt', 'r') as fin:
    data = fin.read().splitlines()  # Read lines into a list, removing newline characters

    for line in data:
        columns = line.split(',')  # Split each line into columns based on comma
        
        if columns:  # Check if there are columns in the line (to handle potential empty lines)
            first_value = columns[0].strip()  # Get the first column value and strip whitespace
            first_column.append(float(first_value))  # Convert to float and add to first_column list

print("First column values:")
for value in first_column:
    print(value)

# If we want each value to be on a newline: 

with open('input_text.txt', 'r') as fin:
    data = fin.read().splitlines()  # Read lines into a list, removing newline characters

    for line in data:
        columns = line.split(',')  # Split each line into columns based on comma
        
        # Now you can work with each column data
        for column in columns:
            print(column.strip())  # Print each column value (strip to remove any surrounding whitespace)
