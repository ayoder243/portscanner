import socket
import termcolor


def scan(targets, port_list):
  for target in targets:
    print(termcolor.colored('\n[*] Scanning ' + target, 'green'))
    for port in port_list:
      scan_port(target, port)

def scan_port(ipaddress, port):
  try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print(termcolor.colored('[+] Port Open: ' + str(port), 'blue'))
    sock.close()
  except:
    pass

def create_port_list(ports):
  port_list = []
  for port in ports:
    if '-' in port:
      port = port.split('-')
      start = int(port[0])
      end = int(port[1])
      port_range = [int(i) for i in range(start, end)]
      port_list.extend(port_range)
    else:
      port_list.append(int(port))
  return port_list


targets = input('[*] Enter Target To Scan (split by ,): ').split(',')
ports = input('[*] Enter The Ports You Want To Scan (ranges(1-100) and csv): ').split(',')
port_list = create_port_list(ports)
scan(targets, port_list)
