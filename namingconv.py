# File Naming Convention for IP Addresses

def increment_sequence(filenames, start_sequence):
    ip_sequence = {}  # Dictionary to store the last sequence number for each unique IP address

    new_filenames = []  # List to store the new filenames

    for filename in filenames:
        ip_address, sequence = filename.split('_')  # Split filename into IP address and sequence number
        sequence = int(sequence.split('.')[0])  # Remove file extension and convert sequence to integer

        if ip_address not in ip_sequence:
            ip_sequence[ip_address] = start_sequence
            start_sequence += 4
        else:
            ip_sequence[ip_address] += 0
            ip_sequence[ip_address] = ip_sequence[ip_address] + 10000

        new_filenames.append(f"{ip_address}_{ip_sequence[ip_address]:06}.txt")  # Generate new filename and append to list

    return new_filenames

# Example usage

filenames = [
    "10.0.1.1_003010.txt",
    "10.0.1.1_013010.txt",
    "10.0.1.1_023010.txt",
    "172.16.2.2_003014.txt",
    "172.16.2.2_013014.txt",
    "172.16.2.2_023014.txt",
    "192.168.3.3_003018.txt"
]
start_sequence = 3010

new_filenames = increment_sequence(filenames, start_sequence)
for filename in new_filenames:
    print(filename)
