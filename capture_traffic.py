# The script uses the sniff function from the scapy library to capture network packets. It sets a filter to only capture IP packets (filter="ip"). 
# The prn parameter specifies a callback function (process_packet) that will be called for each captured packet.

from scapy.all import sniff, IP

# Create a callback function to process captured packets
def process_packet(packet):
    if IP in packet:
        # Extract relevant information from the packet
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Perform analysis or actions based on the extracted information
        # Example: Print the source and destination IP addresses
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        print("")

# Capture network packets using a sniffing function
sniff(filter="ip", prn=process_packet)
