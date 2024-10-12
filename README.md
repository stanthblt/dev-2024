# TP3 DEV : Premiers pas Python

Dans ce premier TP, on va se familiariser avec quelques notions Python, en faisant des trucs de réseau. Promis on fait des trucs plus intéressants après, mais on commence simple pour les premiers pas avec Python.

## Sommaire

- [TP3 DEV : Premiers pas Python](#tp3-dev--premiers-pas-python)
  - [Sommaire](#sommaire)
- [I. Ping](#i-ping)
- [II. DNS](#ii-dns)
- [III. Get your IP](#iii-get-your-ip)
- [IV. Mix](#iv-mix)
- [V. Logs](#v-logs)
- [VI. Deploy](#vi-deploy)

# I. Ping

🌞 **`ping_simple.py`**

---

🌞 **`ping_arg.py`**

🌞 **`is_up.py`**

# II. DNS

🌞 **`lookup.py`**

# III. Get your IP

🌞 **`get_ip.py`**

# IV. Mix

🌞 **`network.py`**

# V. Logs

🌞 **Continuez sur le script précédent `network.py`**

# VI. Deploy

🌞 **Déployez-moi ça dans une VM Rocky**

```bash
[et0@localhost ~]$ pip3 install psutil
Defaulting to user installation because normal site-packages is not writeable
Collecting psutil
  Downloading psutil-6.0.0-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (292 kB)
     |████████████████████████████████| 292 kB 1.1 MB/s 
Installing collected packages: psutil
  WARNING: Value for scheme.platlib does not match. Please report this to <https://github.com/pypa/pip/issues/10151>
  distutils: /home/patron/.local/lib/python3.9/site-packages
  sysconfig: /home/patron/.local/lib64/python3.9/site-packages
  WARNING: Additional context:
  user = True
  home = None
  root = None
  prefix = None
Successfully installed psutil-6.0.0
WARNING: You are using pip version 21.2.3; however, version 24.2 is available.
You should consider upgrading via the '/usr/bin/python -m pip install --upgrade pip' command.
```
```bash
[et0@localhost TP3]$ python network.py ping 8.8.8.8
UP !

[et0@localhost TP3]$ sudo cat /tmp/network_tp3/network.log
2024-10-10 11:18:43 [INFO] Command ping called successfully with argument 8.8.8.8.
```