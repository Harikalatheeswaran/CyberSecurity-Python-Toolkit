# 📌 Section 3: Scapy Introduction — Craft & Send ICMP Packet
from scapy.all import IP, ICMP, Raw, sr1

def send_icmp_ping(destination="8.8.8.8", timeout=2):
    print(f"[>] Pinging {destination} with ICMP...")

    packet = IP(dst=destination) / ICMP()

    try:
        reply = sr1(packet, timeout=timeout, verbose=False)
        if reply:
            print(f"[+] Received reply from {reply.src}")
            print(dir(reply))
            print(f"\nData Received from the server :\n{reply.show()}") # to show the packer layer.
        else:
            print("[-] No reply received (timeout)")
            
        # to read the data from the server that packer should have a [Raw] layer. To read that we do
        if reply.haslayer(Raw):
            payload = reply[Raw].load
            print(f"[+] Payload from server: {payload}")
        else:
            print("[-] No payload received in the reply.")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    send_icmp_ping()
