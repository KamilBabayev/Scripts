#!/usr/local/bin/python3.4
""" This script is used to scan given subnet and find ssh open hosts
   then execute given command against those hosts. """

try:
    import paramiko
except ImportError:
    print("Error: ")
    print("paramiko module must be installed in order to use this script")
    print("For further info use this url:  http://www.paramiko.org/installing.html")

from getpass import getpass
import os
import sys
import re

username = input("Enter username: ")
password = getpass()
result_file = input("Please enter filename for result to writen in: ")


#username="cisco"
#password="cisco"
#command = input("Enter Cisco Command: ")

cmdlist=[]
while True:
    cmd = input("Enter cisco command or type exit if finished: ")
    if cmd == "exit":
        print("Exiting...")
        break
    else:
        cmdlist.append(cmd)
    print(cmdlist)

cmd01 = 'show version | in Model'

if os.path.exists("ips.txt"):  os.system("rm -rf ips.txt")


for i in range(1, 10):
    print("Scanning network range.... Be patient please...")
    awk = " awk {'print $2'}"
    cmd = """ nmap -O -p22  10.50.5.{0} | grep -i 'Cisco IOS' | {1} """.format(i, awk)
#    if os.system(cmd) == "Cisco":
    if os.popen(cmd).read().strip() == "Cisco":
        print("Cisco device found:  10.50.5." + str(i))
        file = open("ips.txt", 'a')
        file.write("10.50.5." + str(i))
        file.write("\n")
        file.close()



ip_file = open('ips.txt')     #Add ip addresses which you want to be connected
port = 22

#cmd01 = 'show ip interface brief'
#cmd02 = 'show version'

sshconn = paramiko.SSHClient()
sshconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
   for ip in ip_file.readlines():
       sshconn.connect(ip, username=username, password=username, look_for_keys=False, allow_agent=False)
       sshconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       stdin, stdout, stderr = sshconn.exec_command(cmdlist[0])
       fd = open(result_file, 'a')
       fd.writelines(ip)
       for line in stdout.readlines():
           print(line)
           fd.writelines(line)
       fd.writelines("---------------------------------------------------\n")
       fd.close()

       sshconn.connect(ip, username=username, password=username, look_for_keys=False, allow_agent=False)
       sshconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       stdin, stdout, stderr = sshconn.exec_command(cmdlist[1])
       for line in stdout.readlines():
            print(line)

       sshconn.connect(ip, username=username, password=username, look_for_keys=False, allow_agent=False)
       sshconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       stdin, stdout, stderr = sshconn.exec_command(cmdlist[2])
       for line in stdout.readlines():
            print(line)

except paramiko.ssh_exception.AuthenticationException:
    print("Username or password is not correct  ")
    sys.exit()
