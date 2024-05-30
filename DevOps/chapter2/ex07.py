import re

line = 'IP 192.168.222.1.65216 > maan-virtual-machine.ssh: Flags [P.], seq 5729:5845, ack 7120, win 4098, length 116'
m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
print(m.group('IP'))