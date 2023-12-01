import re

# 读取nmap扫描结果的文本
with open('IP.txt', 'r') as file:
    data = file.read()

# 使用正则表达式匹配IP地址
ip_addresses = re.findall(r'[0-9]+(?:\.[0-9]+){3}', data)

# 指定保存目录和文件名
save_path = '/home/anon/'
file_name = 'nmap-ip.txt'

# 将匹配到的IP地址写入文件
with open(save_path + file_name, 'w') as file:
    for ip in ip_addresses:
        file.write(ip + '\n')

# 输出匹配到的IP地址
for ip in ip_addresses:
    print(ip)
