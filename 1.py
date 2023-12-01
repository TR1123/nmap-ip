import re
import socket

# 读取包含IP地址的文本
with open('nmap-ip.txt', 'r') as file:
    ip_data = file.read()

# 使用正则表达式匹配IP地址
ip_addresses = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip_data)

# 指定要扫描的端口
port_to_scan = 3389

# 扫描IP地址的指定端口
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

# 显示开放的端口并保存到指定目录
save_path = '/home/anon/in/'
file_name = 'open_ports.txt'

with open(save_path + file_name, 'w') as file:
    for ip in ip_addresses:
        if scan_port(ip, port_to_scan):
            print(f"IP {ip} 端 {port_to_scan} 开")
            file.write(f"IP {ip} 端 {port_to_scan} 开\n")
