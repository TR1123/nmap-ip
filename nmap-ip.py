import argparse
import subprocess
import os

os.system("clear")
os.system("figlet TR1123😊")

# 添加介绍信息
print("\033[94m这是一个简单的nmap脚本，用于过滤出nmap扫描出的IP并检测端口开放，一些简单的命令介绍\033[0m")
print("\033[94m-e\033[0m是指定的包含IP地址的文本文件路径，你也可以自行添加，\033[30m-w\033[0m是指定保存文件的目录路径，\033[91m-cn\033[0m以中文显示所有命令参数，\033[91m-h\033[0m显示所有命令参数")
print("\033[94m祝你使用愉快,后续我会继续开发一些命令\033[0m")

# 创建命令行解析器
parser = argparse.ArgumentParser(description='nmap_ip')
parser.add_argument('program_number', type=int, choices=[1, 2], help='要运行的程序编号（1 或 2）')
parser.add_argument('-e', '--ip_file', help='指定包含IP地址的文本文件路径')
parser.add_argument('-w', '--save_path', help='指定保存文件的目录路径')
parser.add_argument('-cn', '--chinese_help', action='store_true', help='以中文文字显示帮助信息')
args = parser.parse_args()

# 如果指定了 -cn 参数，则以中文文字显示帮助信息
if args.chinese_help:
    print("这里是帮助信息的中文版本")
else:
    # 根据参数运行不同的程序
    if args.program_number == 1:
        if args.ip_file and args.save_path:
            command = f"python 1.py -e {args.ip_file} -w {args.save_path}"
            subprocess.run(command, shell=True)
        else:
            print("请提供必要的参数 -e 和 -w")
    elif args.program_number == 2:
        if args.ip_file and args.save_path:
            command = f"python 2.py -e {args.ip_file} -w {args.save_path}"
            subprocess.run(command, shell=True)
        else:
            print("请提供必要的参数 -e 和 -w")
    else:
        print("无效的程序编号")

# 要传递的参数
nmapip = "your_nmapip_value_here"

# 构建命令
msf_command = f"msfconsole -n {nmapip}"

# 调用工具
subprocess.run(msf_command, shell=True)

# 询问用户是否清除终端上的内容
choice = input("是否清除终端上所有的内容？(y 是 n 不) ")
if choice.lower() == 'y':
    clear_terminal()
