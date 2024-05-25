def generate_filenames(ip_addresses, start_sequence):
    filenames = []
    ip_counters = {}  # Dictionary to store the counter for each IP address
    ip_sequence = {}  # Dictionary to store the last sequence number for each unique IP address

    for ip_address in ip_addresses:
        if ip_address not in ip_sequence:
            ip_sequence[ip_address] = start_sequence
            start_sequence += 4
        else:
            ip_sequence[ip_address] += 10000  # Increment by 10000 for subsequent files for the same IP

        filename = f"{ip_address}_{ip_sequence[ip_address]:06}.txt"
        filenames.append(filename)

    return filenames

# Example usage
ip_addresses = ["10.0.1.1", "10.0.1.1", "10.0.1.1", "172.16.2.2", "172.16.2.2", "172.16.2.2", "192.168.3.3"]
start_sequence = 3010

filenames = generate_filenames(ip_addresses, start_sequence)
for filename in filenames:
    print(filename)
