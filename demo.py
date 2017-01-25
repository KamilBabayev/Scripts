#!/usr/bin/env python3
from netmiko import ConnectHandler
from datetime import datetime

start_time = datetime.now()
print("Script started at: ", start_time)

sw2960 = {
	'device_type':'cisco_ios', 
	'ip':'192.168.5.57', 
	'username':'demo123', 
	'password': 'demo123'
}

sw2950 = {
    'device_type':'cisco_ios',
    'ip':'192.168.5.57',
    'username':'demo123',
    'password': 'demo123'
}

sw6500 = {
	'device_type':'cisco_ios',
	'ip':	'192.168.5.111',
	'username': 'demo123',
	'password': 'demo123',
}

devices = [sw2950, sw2960, sw6500]

def show(device):
	conn = ConnectHandler(**device)
	conn.enable()
	data = conn.send_command('show version | inc System serial')
	data2 = conn.send_command('show arp')
	print('*' * 45)
	print(data)
	print(data2)

for device in devices:
	show(device)

end_time = datetime.now()
print("Script stopped at: ", end_time)

total_time = end_time - start_time 
print("Total time spent for job", total_time)
