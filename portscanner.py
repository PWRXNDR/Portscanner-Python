import socket
import termcolor


def scan(target, ports):
    print('\n' + f'Starting Scan for {target}')
    for port in range(1, ports):
        scan_port(targets, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'[+] Port Opened {port}')
        sock.close()
    except:
        pass


targets = input('[*] Enter target to scan(split them by comma): ')
ports = int(input('[*] Enter how many Ports you want to scan: '))
if ',' in targets:
    print(termcolor.colored(('[*] Scanning multiple Targets'), 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
