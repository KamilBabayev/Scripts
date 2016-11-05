#!/usr/bin/env python3
cmd=input('enter remote command: ')
subnet='192.168.12.'

import re
import paramiko
username='username_here'
password='password_here'

def ssh_conn(host,cmd):
        conn=paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(host, username=username, password=password, \
                                  look_for_keys=False, allow_agent=False)

        stdin,stdout,stderr = conn.exec_command(cmd)
        for  i in stdout:
                line = i.rstrip()
                #if re.search('inet ', line):
                print(line)

for i in range(1,255):
        try:
                print('Executing command on - ', subnet + str(i) , '\n')
                ssh_conn(subnet+str(i), cmd)
                print('\n')
        except paramiko.ssh_exception.NoValidConnectionsError:
                print('could not connect to host')
                print('\n')
        except paramiko.ssh_exception.AuthenticationException:
                print('Authentication Failed')
                print('\n')
        except:
                print('Unexpected error happened')

