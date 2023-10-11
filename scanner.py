import socket
import ipaddress
import argparse
import threading
import time
import nmap
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from utilities.banner_grabber import grab_banner
from utilities.stealth_scanner import stealth_scan

# Service Detection
def detect_service(ip, port):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments=f'-p {port}')
    try:
        return nm[ip]['tcp'][port]['name']
    except:
        return "unknown"

# Port Scanning with banner grabbing
def port_scanning(ip, port, output_file, scan_results):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        s.connect((ip, port))
        banner = grab_banner(ip, port)
        service_name = detect_service(ip, port)
        if banner:
            result = f"[+] Found open port {port} on {ip} with banner: {banner.decode('utf-8')} running {service_name}"
        else:
            result = f"[+] Found open port {port} on {ip} running {service_name}"
        logging.info(result)
        scan_results.append({"ip": ip, "port": port, "banner": banner, "service": service_name})
    except:
        pass

# Scanning target
def scan_target(ip, port, output_file, scan_results):
    start_time = time.time()
    
    if args.stealth:
        stealth_scan(ip, port, output_file)
    else:
        port_scanning(ip, port, output_file, scan_results)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < rate_limit:
        time.sleep(rate_limit - elapsed_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhanced Network Scanner")
    parser.add_argument("-ip", "--iprange", help="IP range to scan. Example: 192.168.1.0/24", required=True)
    parser.add_argument("-p", "--ports", type=int, nargs='+', help="Space-separated list of ports to scan. Example: 22 80 443")
    parser.add_argument("-r", "--rate", type=float, default=0, help="Delay in seconds between each scan. Example: 0.1")
    parser.add_argument("-o", "--output", type=str, default="results/scan_results.txt", help="File to save scan results. Default is 'results/scan_results.txt'")
    parser.add_argument("--stealth", help="Use stealth SYN scan", action="store_true")
    parser.add_argument("--log", help="Enable logging", action="store_true")

    args = parser.parse_args()
    ip_range = args.iprange
    ports = args.ports
    rate_limit = args.rate
    output_file = args.output

    if args.log:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    scan_results = []

    # Use ThreadPool for efficient scanning
    MAX_THREADS = 50
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for ip in ipaddress.ip_network(ip_range, strict=False):
            for port in ports:
                executor.submit(scan_target, str(ip), port, output_file, scan_results)

    # Save results in JSON format
    with open(output_file, 'w') as outfile:
        json.dump(scan_results, outfile, indent=4)
