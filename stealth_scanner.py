from scapy.all import SYN, IP, sr1

def stealth_scan(ip, port, output_file):
    pkt = IP(dst=ip)/SYN(dport=port)
    resp = sr1(pkt, timeout=2, verbose=0)
    
    if resp and (int(resp.getlayer("TCP").flags) == 18):  # Check for SYN-ACK flags
        result = f"[+] Found open port {port} on {ip} (Stealth Mode)"
        print(result)
        with open(output_file, "a") as file:
            file.write(result + "\n")
