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
  for port in ports:
    if '-' in port:
      port = port.split('-')
      start = int(port[0])
      end = int(port[1])
      port_range = [int(i) for i in range(start, end)]
      port_list.extend(port_range)
    else:
      port_list.append(int(port))
  return 0

target_file_path = ''
port_file_path = ''
targets = ''
ports = ''

for i in range(1, len(sys.argv), 2):
  if sys.argv[i] == '--target-file':
    target_file_path = sys.argv[i+1]
  elif sys.argv[i] == '--port-file':
    port_file_path = sys.argv[i+1]
  elif sys.argv[i] == '--targets':
    targets = sys.argv[i+1].split(',')
  elif sys.argv[i] == '--ports':
    ports = sys.argv[i+1].split(',')

port_list = []

if ports != '':
  create_port_list(ports)
if port_file_path != '':
  with open(port_file_path, 'r') as port_file:
    lines = port_file.readlines()
    for line in lines:
      line = line.replace('\n', '')
      if ',' in line:
        for i in line.split(','):
          port_list.append(int(i))
      elif '-' in line:
        line = line.split('-')
        start = int(line[0])
        end = int(line[1])
        port_range = [int(i) for i in range(start, end)]
        port_list.extend(port_range)
      else:
        port_list.append(line)
print(port_list, targets)
if targets != '':
  scan(targets, port_list)

