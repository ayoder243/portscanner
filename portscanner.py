import socket
import termcolor


def scan(targets, ports):
  for target in targets:
    print(termcolor.colored('\n[*] Scanning ' + target, 'green'))
    for port in range(1, int(ports)):
      scan_port(target, port)

def scan_port(ipaddress, port):
  try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print(termcolor.colored('[+] Port Open: ' + str(port), 'blue'))
    sock.close()
  except:
    pass

targets = input('[*] Enter Target To Scan (split by ,): ').split(',')
ports = input('[*] Enter How May Ports You Want To Scan: ')
scan(targets, ports)



######### Features to Add #############
# 1. Use port ranges and comma separated values
# 2. Get targets from file
# 3. Get ports from file
# 4. Use command line arguments instead of inputs
# 5. Output to file
# 6. Get banner of port