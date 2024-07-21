# Example 1: Parsing time values from a .txt file containing ping result:

# Example input:

# Answer from 127.0.0.1 tries=1 Time=1s id=1
# Answer from 127.0.0.1 tries=1 Time=2s id=1
# Answer from 127.0.0.1 tries=1 Time=15s id=1
# Answer from 127.0.0.1 tries=1 Time=12s id=1
# Answer from 127.0.0.1 tries=1 Time=4s id=1

# Method 1: Using regex

import re
import os

with open("file.txt") as f:
    times = re.findall(r"Time=(\d+)s", f.read())
    print(times)

# ['1', '2', '15', '12', '4']

# Method 2: Storing the 4th element of the split line

import os

times = []
with open("file.txt", "rt") as file:                
    for line in file: 
        times.append(line.split(" ")[4])


# Example 2: Print all lines containing the substring 'error':

errors = []                       # The list where we will store results.
linenum = 0
substr = "error".lower()          # Substring to search for.
with open ('logfile.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
for err in errors:
    print(err)

# Input (stored in logfile.txt):

# This is line 1
# This is line 2
# Line 3 has an error!
# This is line 4
# Line 5 also has an error!

# Output:

# Line 3: Line 3 has an error!
# Line 5: Line 5 also has an error!

# Example 3: Extract all lines containing the substring 'error':

import re
errors = []
linenum = 0
pattern = re.compile("error", re.IGNORECASE)  # Compile a case-insensitive regex
with open ('logfile.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            errors.append((linenum, line.rstrip('\n')))
for err in errors:                            # Iterate over the list of tuples
    print("Line " + str(err[0]) + ": " + err[1])

# Output:

Output:

# Line 6: Mar 28 09:10:37 Error: cannot contact server. Connection refused.
# Line 10: Mar 28 10:28:15 Kernel error: The specified location is not mounted.
# Line 14: Mar 28 11:06:30 ERROR: usb 1-1: can't set config, exiting.

# Example 3:

# Input:

# ['data/earthpy-downloads/avg-monthly-temp-fahr/San-Diego/San-Diego-1999-temp.csv',
# 'data/earthpy-downloads/avg-monthly-temp-fahr/San-Diego/San-Diego-2000-temp.csv',
# 'data/earthpy-downloads/avg-monthly-temp-fahr/San-Diego/San-Diego-2001-temp.csv',
# 'data/earthpy-downloads/avg-monthly-temp-fahr/San-Diego/San-Diego-2002-temp.csv',
# 'data/earthpy-downloads/avg-monthly-temp-fahr/San-Diego/San-Diego-2003-temp.csv']

# Get file name

year_path = sd_data[0]
file_name = os.path.basename(year_path)
print(file_name)

# Output: San-Diego-1999-temp.csv

# Parse a date from file name

year = file_name[10:14]
print(year)

# Output: 1999

# Example 4: Parsing a server log file (server.log)

# Method 1:  Using the re module

import re

log_file = 'server.log'

with open(log_file, 'r') as file:
    for line in file:
        match = re.match(
            r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+)', line)
        if match:
            timestamp = match.group(1)
            severity = match.group(2)
            message = match.group(3)
            # Process extracted information as needed
            print(
                f"Timestamp: {timestamp}, Severity: {severity}, Message: {message}")

# Output:

# Timestamp: 2024-03-10 08:30:15, Severity: INFO, Message: Server
# Timestamp: 2024-03-10 08:35:21, Severity: ERROR, Message: Internal
# Timestamp: 2024-03-10 08:40:02, Severity: WARNING, Message: Disk
# Timestamp: 2024-03-10 08:45:10, Severity: INFO, Message: User
# Timestamp: 2024-03-10 08:50:55, Severity: INFO, Message: Request
# Timestamp: 2024-03-10 08:55:32, Severity: ERROR, Message: Connection

# Method 2: Using the split() method

log_file = 'server.log'

with open(log_file, 'r') as file:
    for line in file:
        parts = line.split(' ', 2)  # Split only on the first two spaces
        if len(parts) < 3:
            continue  # Skip lines that don't have enough parts
        
        timestamp = parts[0] + ' ' + parts[1]  # Combine date and time
        severity = parts[2].split(' ', 1)[0]  # Extract severity
        message = parts[2].split(' ', 1)[1] if ' ' in parts[2] else ''  # Extract message
        
        # Process extracted information as needed
        print(f"Timestamp: {timestamp}, Severity: {severity}, Message: {message}")

  # Output:

# Timestamp: 2024-03-10 08:30:15, Severity: INFO, Message: Server started successfully
# Timestamp: 2024-03-10 08:35:21, Severity: ERROR, Message: Internal server error occurred
# Timestamp: 2024-03-10 08:40:02, Severity: WARNING, Message: Disk space is running low
# Timestamp: 2024-03-10 08:45:10, Severity: INFO, Message: User 'john_doe' logged in
# Timestamp: 2024-03-10 08:50:55, Severity: INFO, Message: Request received: GET /api/data
# Timestamp: 2024-03-10 08:55:32, Severity: ERROR, Message: Connection timeout while processing request
