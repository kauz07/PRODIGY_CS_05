from scapy.all import *

def packet_callback(packet):
    # Extract relevant information from the packet
    source_ip = packet[IP].src
    dest_ip = packet[IP].dst
    protocol = packet[IP].proto
    payload = packet[TCP].payload

    # Display the information
    print(f"Source IP: {source_ip} | Destination IP: {dest_ip} | Protocol: {protocol}")
    if len(payload) > 0:
        print("Payload:", payload)

def main():
    print("Packet Sniffer is running. Press Ctrl+C to stop.")

    # Start sniffing packets
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
