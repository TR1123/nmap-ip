import argparse
import subprocess
import os

print("社交账号：")
print("Twitter：@Fridu60529819")
print("Telegram：t.me/AnonymousTR1123")

os.system("clear")
os.system("figlet TR1123😊")


import argparse
import subprocess
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

os.system("clear")
os.system("figlet TR1123😊")

# 添加介绍信息
print("\033[94m这是一个简单的nmap脚本，用于过滤出nmap扫描出的IP段，并检测3389端口开放，我开发它只是为了好玩😊\033[0m")
print("\033[94m-e\033[0m僵尸网络程序用于扫描指定IP开放端口，你也可以自行添加端口，\033[30m-w\033[0m是指定保存文件的目录路径，\033[91m-cn\033[0m以中文显示所有命令参数，\033[91m-h\033[0m显示所有命令参数")
print("\033[94m祝你使用愉快,后续我会继续开发一些命令\033[0m")

# 创建命令行解析器
parser = argparse.ArgumentParser(description='nmap_ip')
parser.add_argument('program_number', type=int, choices=[1, 2], help='要运行的程序编号（1 或 2）')
parser.add_argument('-e', '--ip_file', help='指定包含IP地址的文本文件路径')
parser.add_argument('-w', '--save_path', help='指定保存文件的目录路径')
parser.add_argument('-cn', '--chinese_help', action='store_true', help='以中文显示帮助')
args = parser.parse_args()

# 如果指定了 -cn 参数，中文显示帮助信息
if args.chinese_help:
    print("中文")
else:
    # 运行不同的程序
    if args.program_number == 1:
        if args.ip_file and args.save_path:
            command = f"python 1.py -e {args.ip_file} -w {args.save_path}"
            subprocess.run(command, shell=True)
        else:
            print("提供必要的参数 -e 和 -w")
    elif args.program_number == 2:
        if args.ip_file and args.save_path:
            command = f"python 2.py -e {args.ip_file} -w {args.save_path}"
            subprocess.run(command, shell=True)
        else:
            print("提供必要的参数 -e 和 -w")
    else:
        print("无效的程序编号")

# 参数
nmapip = "your_nmapip_value_here"

# 命令
msf_command = f"msfconsole -n {nmapip}"

subprocess.run(msf_command, shell=True)
 
choice = input("是否清除终端上所有的内容？(y 是 n 不) ")
if choice.lower() == 'y':
    clear_terminal()
