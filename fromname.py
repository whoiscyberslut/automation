import os

def extract_info_from_document(document):
    # Splitting the document into lines
    lines = document.split("\n")
        # Now, lines is a list containing each line of the document as an element:
# ['',
#  'pings  target   min/avg/max/mdev',
#  '===================================',
#  '9      8.8.4.4  4.33/4.39/4.43/0.03',
#  '7      8.8.4.4  4.37/4.39/4.41/0.06',
#  '12     8.8.8.8  4.22/4.30/4.34/0.08',
#  '3      8.8.8.8  4.29/4.29/4.29/0.08',
#  '']
    # Assuming the first two lines are headers
    # Extracted Headers: ['pings', 'target', 'min/avg/max/mdev']
    headers = lines[0].split()
    # Initializing an empty list to store extracted data
    data = []
    # Looping through each line starting from the third line
    for line in lines[2:]:
        parts = line.split() # Splitting the line into parts
        # Filter out empty lines
        if parts:
            # Check if the line has enough parts to parse
            if len(parts) >= 3:
                # Try to parse ping count, target IP, and statistics
                ping = int(parts[0]) # Converting ping count to integer
                target = parts[1] # Extracting target IP
                stats = parts[2].split('/') # Splitting statistics into individual parts
                # Check if statistics are complete (min/avg/max/mdev)
                if len(stats) == 4:
                    stats = [float(stat) for stat in stats] # Converting statistics to floating-point numbers
                    # Appending the extracted information as a dictionary to the data list
                    data.append({'ping': ping, 'target': target, 'stats': stats})  
                else:
                    print("Incomplete statistics in line:", line)
            else:
                print("Incomplete line:", line)
        else:
            print("Empty line detected.")
    return headers, data

# After the loop, data contains the extracted information in the following format:
# [{'ping': 9, 'target': '8.8.4.4', 'stats': [4.33, 4.39, 4.43, 0.03]},
#  {'ping': 7, 'target': '8.8.4.4', 'stats': [4.37, 4.39, 4.41, 0.06]},
#  {'ping': 12, 'target': '8.8.8.8', 'stats': [4.22, 4.30, 4.34, 0.08]},
#  {'ping': 3, 'target': '8.8.8.8', 'stats': [4.29, 4.29, 4.29, 0.08]}]

# Finally, the function returns the extracted headers and data
# Headers: ['pings', 'target', 'min/avg/max/mdev']
# Data: [{'ping': 9, 'target': '8.8.4.4', 'stats': [4.33, 4.39, 4.43, 0.03]},
#        {'ping': 7, 'target': '8.8.4.4', 'stats': [4.37, 4.39, 4.41, 0.06]},
#        {'ping': 12, 'target': '8.8.8.8', 'stats': [4.22, 4.30, 4.34, 0.08]},
#        {'ping': 3, 'target': '8.8.8.8', 'stats': [4.29, 4.29, 4.29, 0.08]}]

def read_document_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

# Function to extract target IP addresses from data (a list of dictionaries), returning them as a separate list.
def extract_targets(data):
    return [entry['target'] for entry in data]   # Extracting 'target' values from data entries

# Function to aggregate results from multiple files in a directory
def aggregate_results(directory):
    ip_results = {} # Initializing an empty dictionary to store aggregated results

    for filename in os.listdir(directory):  # Looping through files in the directory
        if filename.endswith('.txt'):  # Checking if the file is a text file
            # Extract IP address from filename
            parts = filename.split('_')
            if len(parts) != 2:
                print(f"Skipping invalid filename: {filename}")
                continue
            ip_address = parts[0] # IP address is the part before the underscore, given the file is titled, e.g., 10.0.1.1_003014.txt
            filepath = os.path.join(directory, filename) # Constructing full file path
            headers, data = extract_info_from_document(read_document_from_file(filepath))
            if ip_address not in ip_results:
                ip_results[ip_address] = []  # If it's not present, a new empty list is created for that IP address. 
            ip_results[ip_address].extend(data)
    return ip_results

def write_combined_dataset(aggregated_directory, ip_results):
    if not os.path.exists(aggregated_directory):
        os.makedirs(aggregated_directory)
    print("Creating directory '{}' ... done.".format(aggregated_directory))

    print("IP addresses encountered:")
    for ip_address, data in ip_results.items(): # This loop iterates over each key-value pair in the ip_results dictionary. Each key represents an IP address, and the associated value is a list of data entries related to that IP address.
        print(" -", ip_address) # This line prints each IP address encountered during the aggregation process. The - is used as a prefix to each IP address for formatting.
        combined_data = "\n".join(["\t".join(map(str, [entry['ping']] + entry['stats'])) for entry in data])
        with open(os.path.join(aggregated_directory, f"{ip_address}.txt"), 'w') as file:
            file.write(combined_data)
        print(f"Writing combined dataset to '{os.path.join(aggregated_directory, ip_address + '.txt')}'... done.")
    print("Aggregation completed!")

directory = '/Users/user/dir'  # Change this to your desired directory
print("Parsing experiment result files in directory: {} ...".format(directory))
aggregated_directory = os.path.join(directory, 'aggregated')
ip_results = aggregate_results(directory)
write_combined_dataset(aggregated_directory, ip_results)
