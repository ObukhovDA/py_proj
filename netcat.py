import argparse 
import socket 
import shlex 
import subprocess 
import sys 
import textwrap 
import threading 

def execute(cmd): 
    cmd = cmd.strip() 
    if not cmd: 
        return 
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT) 

    return output.decode() 

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        description='BHP Net Tool', 
        formatter_class=argparse.RawDescriptionHelpFormatter, 
        epilog=textwrap.dedent('''Example: 
                               netcat.py -t 192.168.1.108 -p 5555 -l -c # командная оболочка 
                               netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt 
                               # загружаем в файл 
                               netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"
                               # выполянем команду 
                               echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 
                               # шлем текст на порт севрера 135 
                               netcat.py -t 192.168.1.108 -p 5555 # соединяемся с сервером 
                               ''')) 
    parser.add_argument('-c', '--command', action='store_true', 
                        help='command shell') 
    parser.add_argument('-e', '--execute', help='execute specified command') 
    parser.add_argument('-l', '--listen', action='store_true', help='listen') 
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port') 
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP') 
    parser.add_argument('-u', '--upload', help='upload file') 
    args = parser.parse_args() 
    if args.listen: 
        buffer = '' 
    else: 
        buffer = sys.stdin.read() 

    nc = NetCat(args, buffer.encode()) 
    nc.run() 

