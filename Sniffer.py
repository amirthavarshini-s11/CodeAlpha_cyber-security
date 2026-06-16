import time
import random

print("=========================================")
print("  MOCK NETWORK SNIFFER STARTING...       ")
print("  Waiting for network traffic...         ")
print("=========================================")
time.sleep(1.5)

ips = ["192.168.1.1", "192.168.1.45", "10.0.0.4", "172.217.16.142", "142.250.190.46"]
protocols = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS"]

for i in range(1, 11):
    src = random.choice(ips)
    dst = random.choice(ips)
    while src == dst:
        dst = random.choice(ips)
        
    proto = random.choice(protocols)
    length = random.randint(44, 1500)
    
    print(f"[+] Packet #{i}: {src} -> {dst}")
    print(f"    Protocol: {proto} | Size: {length} bytes")
    print("-" * 40)
    time.sleep(1)

print("\n[✔] Sniffing completed! 10 Packets processed.")
