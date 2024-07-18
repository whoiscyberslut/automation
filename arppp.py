import re
import subprocess

def get_mac(ip):
    """
    Get the MAC address for a given IP address using the arp command.
    """
    arp_cmd = ["arp", ip]
    mac_pattern = re.compile(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}")

    try:
        # Execute the arp command
        output = subprocess.check_output(arp_cmd, text=True)

        # Search for the MAC address in the output
        match = mac_pattern.search(output)
        if match:
            return match.group(0)
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error executing arp command: {e}")
        return None

if __name__ == "__main__":
    ip = "10.0.1.1"  # IP address to look up #OR: ip = input("Enter the IP address to look up: ") 
    mac_addr = get_mac(ip)
    if mac_addr:
        print(f"MAC address for {ip} is {mac_addr}")
    else:
        print(f"MAC address for {ip} not found")
