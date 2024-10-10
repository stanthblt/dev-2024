import os
from sys import argv


if len(argv) != 2:
    print("Usage: python is_up.py <IP>")
else:
    ip_address = argv[1]
    response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
    if response == 0:
        print("UP !")
    else:
        print("DOWN !")
