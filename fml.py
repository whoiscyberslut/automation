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
