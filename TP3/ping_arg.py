import os
from sys import argv

if len(argv) != 2:
    print("Usage: python ping_arg.py <IP>")
else:
    ip_address = argv[1]
    os.system(f"ping -c 4 {ip_address}")
