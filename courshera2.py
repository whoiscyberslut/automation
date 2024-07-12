import os

def extract_info_from_document(document):
    # Splitting the document into lines
    lines = document.split("\n")
    for index, line in enumerate(lines):
        print(f"Line {index}: '{line}'")
    # Assuming the first two lines are headers
    headers = lines[0].split()
    print("Extracted Headers:", headers)
    headers1 = lines[1].split()
    print("Extracted Headers1:", headers1)
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

def read_document_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def extract_targets(data):
    return [entry['target'] for entry in data]

def aggregate_results(directory):
    ip_results = {}

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # Extract IP address from filename
            parts = filename.split('_')
            if len(parts) != 2:
                print(f"Skipping invalid filename: {filename}")
                continue
            ip_address = parts[0]
            filepath = os.path.join(directory, filename)
            headers, data = extract_info_from_document(read_document_from_file(filepath))
            if ip_address not in ip_results:
                ip_results[ip_address] = []
            ip_results[ip_address].extend(data)
    return ip_results

def write_combined_dataset(aggregated_directory, ip_results):
    if not os.path.exists(aggregated_directory):
        os.makedirs(aggregated_directory)
    print("Creating directory '{}' ... done.".format(aggregated_directory))

    print("IP addresses encountered:")
    for ip_address, data in ip_results.items():
        print(" -", ip_address)
        combined_data = "\n".join(["\t".join(map(str, [entry['ping']] + entry['stats'])) for entry in data])
        with open(os.path.join(aggregated_directory, f"{ip_address}.txt"), 'w') as file:
            file.write(combined_data)
        print(f"Writing combined dataset to '{os.path.join(aggregated_directory, ip_address + '.txt')}'... done.")
    print("Aggregation completed!")

directory = '/Users/user'  # Change this to your desired directory
print("Parsing experiment result files in directory: {} ...".format(directory))
aggregated_directory = os.path.join(directory, 'aggregated')
ip_results = aggregate_results(directory)
write_combined_dataset(aggregated_directory, ip_results)
