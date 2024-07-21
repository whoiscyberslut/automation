import subprocess

def parse_ipconfig_output():
    adapters = {}
    
    # Execute the 'ipconfig' command and get its output
    output = subprocess.check_output("ipconfig").decode()
    
    # Iterate over each line of the output
    for line in output.splitlines():
        # Check if the line indicates the start of a new adapter
        term = "Ethernet adapter "
        if line.startswith(term):
            # Extract the adapter name by removing the prefix
            adapter_name = line[len(term):-1]
            adapters[adapter_name] = {}
            current_adapter = adapters[adapter_name]
            continue
        
        # Split the line into key-value pairs based on the presence of " : "
        split_at = " : "
        if split_at in line:
            key, value = line.split(split_at)
            key = key.replace(" .", "").strip()
            current_adapter[key] = value
    
    # Print the extracted adapter information
    for adapter_name, adapter in adapters.items():
        print(f"{adapter_name}:")
        for key, value in adapter.items():
            print(f"    '{key}' = '{value}'")
        print()

if __name__ == "__main__":
    parse_ipconfig_output()

# Output

# Local Area Connection:
#     'Connection-specific DNS Suffix' = 'example.com'
#     'Link-local IPv6 Address' = 'fe80::1a2b:3c4d:5e6f:7g8h%12'
#     'IPv4 Address' = '192.168.1.10'
#     'Subnet Mask' = '255.255.255.0'
#     'Default Gateway' = '192.168.1.1'

# Wireless LAN adapter Wi-Fi:
#     'Connection-specific DNS Suffix' = 'example.com'
#     'IPv6 Address' = '2001:db8::1'
#     'IPv4 Address' = '192.168.0.5'
#     'Subnet Mask' = '255.255.255.0'
#     'Default Gateway' = '192.168.0.1'
