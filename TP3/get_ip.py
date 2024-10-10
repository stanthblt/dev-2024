import psutil

interfaces = psutil.net_if_addrs()

for interface, addrs in interfaces.items():
    for addr in addrs:
        if addr.family == 2:  
            ip = addr.address
            mask = addr.netmask
            if mask:  
                mask_bits = sum([bin(int(x)).count('1') for x in mask.split('.')])
                cidr = f"{ip}/{mask_bits}"
                available_ips = 2**(32 - mask_bits)
                print(f"{cidr}")
                print(f"{available_ips} adresses")
                break
