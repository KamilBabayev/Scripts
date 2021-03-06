#!/usr/bin/env python3
# This script is example to automate config provisioning of
# cisco switch interfaces via python paramiko module.
# We can gather command groups in some list and iterae this list
# inside function in order to shorten our code. I will rewrite this.
import paramiko
import time
from getpass import getpass

username='cisco'
password='cisco'
# or comment above line and use -  password = getpass()  - to hide password
router_ip='10.94.65.211'
interfaces = [13,14,15]

def cisco_int_config(interface_number):
	conn = paramiko.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	conn.connect(router_ip, username=username, password=password, look_for_keys=False, allow_agent=False)
	console = conn.invoke_shell()
#	console.recv(1024)
	console.send("conf t\n")
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("int Gi 0/{}\n".format(interface_number))
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("description Kamil_python_test_int\n")
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("switchport trunk encapsulation dot1q\n")
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("switchport mode trunk\n")
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("switchport trunk allowed vlan  1,2,30,31,32\n")
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("no shutdown\n")
	time.sleep(.5)
#	print(console.recv(65000))
	console.send("do sh  run int Gi 0/{}\n".format(interface_number))
	time.sleep(.5)
	res = console.recv(65000)
	output = str(res)
	for i in output.strip().split('\\r\\n'):
		line = i.rstrip()
		print(line)

for interface in interfaces:
	cisco_int_config(interface)

