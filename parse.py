import os
import re
import sys

def parse_results(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) < 3:
            return None
        
        ip_address = lines[1].split()[1]
        results = []
        for line in lines[2:]:
            if line.strip():
                parts = line.split()
                if len(parts) == 4:
                    results.append(parts)
        
        return ip_address, results

def aggregate_results(directory):
    ip_results = {}
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            result = parse_results(filepath)
            if result:
                ip_address, data = result
                if ip_address not in ip_results:
                    ip_results[ip_address] = []
                ip_results[ip_address].extend(data)
    
    return ip_results

def write_aggregated_results(aggregated_results, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    for ip_address, data in aggregated_results.items():
        output_filename = os.path.join(output_directory, f"{ip_address}.txt")
        with open(output_filename, 'w') as file:
            file.write(f"pings target min/avg/max/mdev\n")
            for result in data:
                file.write(" ".join(result) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 script.py")
        sys.exit(1)
    
    print("Parsing experiment result files in current directory...")
    aggregated_results = aggregate_results('.')
    print("done.")
    
    output_directory = "aggregated"
    print(f"Creating directory \"{output_directory}\"...", end=" ")
    write_aggregated_results(aggregated_results, output_directory)
    print("done.")
    
    print("IP addresses encountered:")
    for ip_address in aggregated_results.keys():
        print(f"  - {ip_address}")
    
    print("Writing combined dataset to \"aggregated\" directory... done.")
    print("Aggregation completed!")
