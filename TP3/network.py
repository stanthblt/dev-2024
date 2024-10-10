import socket
import psutil
import os
import sys
import platform
from datetime import datetime

if platform.system() == "Windows":
    TEMP_DIR = os.path.join(os.getenv('APPDATA'), 'Local', 'Temp', 'network_tp3')
else: 
    TEMP_DIR = "/tmp/network_tp3"

LOG_FILE = os.path.join(TEMP_DIR, "network.log")

os.makedirs(TEMP_DIR, exist_ok=True)

def write_log(level, command, args=None, error=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if error:
        log_message = f"{timestamp} [ERROR] Command {command} called with bad arguments : {args}.\n"
    else:
        if args:
            log_message = f"{timestamp} [INFO] Command {command} called successfully with argument {args}.\n"
        else:
            log_message = f"{timestamp} [INFO] Command {command} called successfully.\n"
    
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(log_message)

def lookup(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[2]
        return '\n'.join(ip_addresses)
    except socket.gaierror:
        return f"Impossible de trouver le domaine {domain}"

def ping(ip):
    try:
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
        return "UP !" if response == 0 else "DOWN !"
    except Exception as e:
        return f"Erreur ping : {e}"

def ip():
    interface = "en0"
    interfaces = psutil.net_if_addrs()

    if interface in interfaces:
        for addr in interfaces[interface]:
            if addr.family == 2:
                ip_addr = addr.address
                mask = addr.netmask

                if mask:
                    mask_bits = sum([bin(int(x)).count('1') for x in mask.split('.')])
                    available_ips = 2 ** (32 - mask_bits)
                    return f"{ip_addr}\n{available_ips} adresses"
    return "Impossible de récupérer l'adresse IP"

if len(sys.argv) < 2:
    print("Usage: python network.py <command> [arguments]")
else:
    command = sys.argv[1]

    if command == "lookup" and len(sys.argv) == 3:
        result = lookup(sys.argv[2])
        print(result)
        write_log("INFO", "lookup", sys.argv[2])
    elif command == "ping" and len(sys.argv) == 3:
        result = ping(sys.argv[2])
        print(result)
        write_log("INFO", "ping", sys.argv[2])
    elif command == "ip" and len(sys.argv) == 2:
        result = ip()
        print(result)
        write_log("INFO", "ip")
    else:
        print(f"'{command}' is not an available command. Déso.")
        write_log("ERROR", command, ' '.join(sys.argv[1:]), error=True)
