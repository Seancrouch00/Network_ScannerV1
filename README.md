# Network_ScannerV1

An advanced network scanner built with Python. It provides multiple features including port scanning, banner grabbing, service detection, and stealth scanning capabilities.

Features:

- Port Scanning: Detect open ports on target IPs.
- Banner Grabbing: Fetch the banners of open services.
- Service Detection: Identify services running on open ports using `nmap`.
- Stealth Scanning: Perform a stealth SYN scan.
- Multi-threading: Scan multiple ports concurrently for faster results.
- Dynamic Rate Control: Adjust the scan speed based on the responsiveness of the target.
- Output Formats: Save results in JSON format.
- Logging: Detailed logs of the scanning process.

Installation:

1. Clone the repository:
```bash
git clone https://github.com/[YourUsername]/enhanced-network-scanner.git
cd enhanced-network-scanner
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

Usage:

Basic Scan:
To scan a range of IP addresses for specific ports:
```bash
python scanner.py -ip 192.168.1.0/24 -p 22 80 443
```

Stealth Scan:
For a stealthier SYN scan:
```bash
python scanner.py -ip 192.168.1.0/24 -p 22 80 443 --stealth
```

Rate Control:
To introduce a delay between scans, for example, 0.1 seconds:
```bash
python scanner.py -ip 192.168.1.0/24 -p 22 80 443 -r 0.1
```

Output to File:
By default, results are saved to `results/scan_results.txt`. To change the output file:
```bash
python scanner.py -ip 192.168.1.0/24 -p 22 80 443 -o myresults.json
```

Enable Logging:
To enable detailed logging:
```bash
python scanner.py -ip 192.168.1.0/24 -p 22 80 443 --log
```

Dependencies:

- `socket`
- `ipaddress`
- `argparse`
- `threading`
- `time`
- `nmap`
- `json`
- `logging`
- `concurrent.futures`

You can install them using:
```bash
pip install -r requirements.txt
```

Notes:

- Always obtain proper permissions before scanning any network.
- This tool is for educational purposes only. Do not use it for illegal activities.
- Scanning networks without permission can lead to legal consequences.

File Structure:
network_scanner/
│
├── scanner.py                  # Main scanning script
├── utilities/
│   ├── __init__.py             # Initialize the utilities package
│   ├── banner_grabber.py       # Contains the banner grabbing function
│   └── stealth_scanner.py      # Contains the stealth scanning function using scapy
│
└── results/                    # Directory to save scanning results
    └── scan_results.txt       # Default file to save results
