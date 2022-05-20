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

def expand_port_range(port_range):
  port_range = port_range.split('-')
  start = int(port_range[0])
  end = int(port_range[1])
  return [int(i) for i in range(start, end+1)]

def create_port_list(ports):
  port_list = []
  if port_file_path != '':
    ports += ','
    with open(port_file_path, 'r') as port_file:
      lines = port_file.readlines()
      for line in lines:
        ports += line.replace('\n', ',')
  ports = ports.split(',')
  for port in ports:
    if '-' in port:
      port_range = expand_port_range(port)
      port_list.extend(port_range)
    else:
      port_list.append(int(port))
  return sorted(port_list)

def create_target_list(targets):
  target_list = []
  if target_file_path != '':
    targets += ','
    with open(target_file_path, 'r') as target_file:
      lines = target_file.readlines()
      for line in lines:
        targets += line.replace('\n', ',')
  targets = targets.split(',')
  for target in targets:
    target_list.append(target)
  return sorted(target_list)

def get_parameters():
  for i in range(1, len(sys.argv), 2):
    if sys.argv[i] == '--target-file':
      target_file_path = sys.argv[i + 1]
    elif sys.argv[i] == '--port-file':
      port_file_path = sys.argv[i + 1]
    elif sys.argv[i] == '--targets':
      targets = sys.argv[i + 1]
    elif sys.argv[i] == '--ports':
      ports = sys.argv[i + 1]
  return target_file_path, port_file_path, targets, ports

target_file_path, port_file_path, targets, ports = get_parameters()

port_list = create_port_list(ports)

target_list = create_target_list(targets)

scan(target_list, port_list)

