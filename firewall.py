import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"[+] Rule successfully added: {command}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Execution failed for: {command}\nError: {e.stderr.decode().strip()}")

def block_malicious_ip(ip):
    print(f"[*] Appending Drop Rule for Target IP: {ip}")
    run_command(f"sudo iptables -A INPUT -s {ip} -j DROP")

def block_target_port(port, proto="tcp"):
    print(f"[*] Appending Drop Rule for Target Port: {port} ({proto})")
    run_command(f"sudo iptables -A INPUT -p {proto} --dport {port} -j DROP")

def list_active_policies():
    print("\n=== Current Active Netfilter Chain Rules ===")
    subprocess.run("sudo iptables -L -n --line-numbers", shell=True)

def flush_all_policies():
    print("[*] Flushing all custom rules to avoid lockout...")
    run_command("sudo iptables -F")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 firewall.py [block_ip <ip> | block_port <port> | status | clear]")
        sys.exit(1)
        
    action = sys.argv[1]
    if action == "block_ip" and len(sys.argv) == 3:
        block_malicious_ip(sys.argv[2])
    elif action == "block_port" and len(sys.argv) == 3:
        block_target_port(sys.argv[2])
    elif action == "status":
        list_active_policies()
    elif action == "clear":
        flush_all_policies()
    else:
        print("[-] Invalid arguments specified.")
