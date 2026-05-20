## Python-Core-Netfilter-Firewall
A custom Python firewall script that interacts with Linux iptables to dynamically block and manage network traffic.

## Objective
To design and implement a custom Python-based firewall script that interacts with the Linux kernel's `iptables` to dynamically control network traffic. This project demonstrates defensive cybersecurity programming by allowing the automated blocking and unblocking of specific ports and IP addresses. This project was completed as part of a 1-Month Cyber Security Internship.

## Environment & Tools
* **Operating System:** Kali Linux
* **Language:** Python 3
* **Core Modules:** `subprocess`, `sys`
* **Networking Utility:** `iptables` (Netfilter)

## Core Features
* **Block Port:** Drops incoming network packets targeting specific ports (e.g., TCP 8080).
* **Block IP:** Drops incoming network packets from malicious or specified IP addresses.
* **Status Check:** Displays the current active `iptables` netfilter chain rules.
* **Flush Rules:** Clears all custom configurations to prevent permanent network lockout.

---

## Phase 1: Baseline Network Communication
A local Python HTTP server was initiated on port 8080 to establish a baseline for normal network traffic. The server was verified as accessible via the local loopback address (`127.0.0.1`).

> **[ 📸 INSERT SCREENSHOT 1 HERE: Web browser successfully loading the Directory Listing on `127.0.0.1:8080` before the firewall is activated ]**

## Phase 2: Firewall Activation & Traffic Interception
The custom `firewall.py` script was executed with administrative privileges to append a `DROP` rule for TCP traffic on port 8080 (`sudo python3 firewall.py block_port 8080`). 

Upon refreshing the web browser, the connection was successfully intercepted and dropped by the Linux kernel, resulting in a connection timeout. This confirms the successful deployment of the defensive mechanism.

> **[ 📸 INSERT SCREENSHOT 2 HERE: Web browser showing "Connection Timed Out" or "Unable to connect" after the firewall rule is applied ]**

## Phase 3: Network Restoration
To ensure the system is not permanently locked out of essential services, the firewall's flush command (`sudo python3 firewall.py clear`) was executed, successfully wiping the active `iptables` rules and restoring normal network access to the port.
