def extract_info_from_document(document):
    lines = document.split("\n")
    # Assuming the first two lines are headers
    lines = document.split("\n")
    # Assuming the first two lines are headers
    headers = lines[0].split()
    print("Extracted Headers:", headers)
    # Assuming the first two lines are headers
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
                    print([entry['target'] for entry in data])
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

filename = input("Enter the filename: ")
document = read_document_from_file(filename)

headers, data = extract_info_from_document(document)

print("Headers:", headers)
print("Data:")
for entry in data:
    print(entry)

# OR:

import os

def extract_info_from_document(document):
    lines = document.split("\n")
    # Assuming the first line is headers and data starts from the third line
    headers = lines[0].split()
    print("Extracted Headers:", headers)
    data = []
    
    for line in lines[2:]:
        parts = line.split()
        # Filter out empty lines
        if parts:
            # Check if the line has enough parts to parse
            if len(parts) >= 3:
                try:
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
                except ValueError:
                    print("Error converting data:", line)
            else:
                print("Incomplete line:", line)
        else:
            print("Empty line detected.")
    
    # Print targets after processing all lines
    print([entry['target'] for entry in data])
    return headers, data

def read_document_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found:", filename)
        return ""
    except IOError as e:
        print("Error reading file:", filename, "Error:", e)
        return ""

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    document = read_document_from_file(filename)

    if document:
        headers, data = extract_info_from_document(document)
        print("Headers:", headers)
        print("Data:")
        for entry in data:
            print(entry)
