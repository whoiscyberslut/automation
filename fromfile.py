#from file contents

import os
from pathlib import Path

def extract_info_from_document(document):
    lines = document.split("\n")
    # Assuming the first two lines are headers
    headers = lines[0].split()
    data = []
    for line in lines[2:]:
        parts = line.split()
        # Filter out empty lines
        if parts:
            # Check if the line has enough parts to parse
            if len(parts) >= 3:
                # Try to parse ping count, target IP, and statistics
                ping = int(parts[0])
                target = parts[1]
                stats = parts[2].split('/')
                # Check if statistics are complete
                if len(stats) == 4:
                    stats = [float(stat) for stat in stats]
                    data.append({'ping': ping, 'target': target, 'stats': stats})
                else:
                    print("Incomplete statistics in line:", line)
            else:
                print("Incomplete line:", line)
        else:
            print("Empty line detected.")
    return headers, data

def read_document_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def extract_targets(data):
    return [entry['target'] for entry in data]

def aggregate_results(directory):
    ip_results = {}

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            headers, data = extract_info_from_document(read_document_from_file(filepath))
            for entry in data: # This line iterates over each data entry extracted from the document.
                ip_address = entry['target'] # This line extracts the 'target' IP address from the current data entry.
                if ip_address not in ip_results:  # Checking if IP address is not already in results dictionary. 
                    ip_results[ip_address] = []   # If it's not present, a new empty list is created for that IP address. 
                ip_results[ip_address].append(entry) # Then, the current data entry is appended to the list associated with that IP address in the ip_results dictionary.
    return ip_results

def write_combined_dataset(aggregated_directory, ip_results):
    if not os.path.exists(aggregated_directory):
        os.makedirs(aggregated_directory)
    print("Creating directory '{}' ... done.".format(aggregated_directory)) #  This is a method of the string class that formats the string by replacing placeholders with the specified values. 
    # In this case, it replaces {} with the value of aggregated_directory.

    print("IP addresses encountered:")
    for ip_address, data in ip_results.items(): # This loop iterates over each key-value pair in the ip_results dictionary. Each key represents an IP address, and the associated value is a list of data entries related to that IP address.
        print(" -", ip_address) # This line prints each IP address encountered during the aggregation process. The - is used as a prefix to each IP address for formatting.
        combined_data = "\n".join(["\t".join(map(str, [entry['ping']] + entry['stats'])) for entry in data])
        with open(os.path.join(aggregated_directory, f"{ip_address}.txt"), 'w') as file:
            file.write(combined_data)
        print(f"Writing combined dataset to '{os.path.join(aggregated_directory, ip_address + '.txt')}'... done.")
    print("Aggregation completed!")

directory = '/Users/user/dir'
print("Parsing experiment result files in current directory: {} ...".format(directory))
aggregated_directory = os.path.join(directory, 'aggregated')
ip_results = aggregate_results(directory)
write_combined_dataset(aggregated_directory, ip_results)
