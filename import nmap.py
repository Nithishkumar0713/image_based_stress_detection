import nmap

# Top most vulnerable ports (commonly exploited)
VULNERABLE_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy"
}

def scan_vulnerable_ports(target):
    scanner = nmap.PortScanner()

    # Scan only vulnerable ports
    ports = ",".join(str(port) for port in VULNERABLE_PORTS.keys())
    scanner.scan(hosts=target, arguments=f"-sT -p {ports}")

    print(f"\n🔍 Scanning Target: {target}\n")

    found = False

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            for port in scanner[host][proto]:
                state = scanner[host][proto][port]['state']
                if state == "open":
                    found = True
                    print(f"[OPEN] Port {port} ({VULNERABLE_PORTS.get(port)})")

    if not found:
        print("✅ No vulnerable open ports found.")

# ---------- Run ----------
if __name__ == "__main__":
    target = input("Enter IP or Hostname: ")
    scan_vulnerable_ports(target)
