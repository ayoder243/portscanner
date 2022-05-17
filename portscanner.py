import socket
import termcolor
import sys


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

target_file = ''
port_file = ''
targets = ''
ports = ''

for i in range(1, len(sys.argv), 2):
  if sys.argv[i] == '--target-file':
    target_file = sys.argv[i+1]
  elif sys.argv[i] == '--port-file':
    port_file = sys.argv[i+1]
  elif sys.argv[i] == '--targets':
    targets = sys.argv[i+1].split(',')
  elif sys.argv[i] == '--ports':
    ports = sys.argv[i+1].split(',')

port_list = create_port_list(ports)
scan(targets, port_list)
