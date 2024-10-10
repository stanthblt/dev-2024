import socket
from sys import argv

if len(argv) != 2:
    print("Usage: python lookup.py <domain>")
else:
    domain = argv[1]
    try:
        ip_address = socket.gethostbyname(domain)
        print(ip_address)
    except socket.gaierror:
        print(f"Impossible de résoudre le domaine {domain}")
