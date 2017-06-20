#!/usr/bin/python
# Here I use fabric tool  as python library to automate some remote and local tasks
# I have installed paramiko, then fabric. fabric works iwith python2.7 more stable.

from fabric import tasks
from fabric.api import *

#env.hosts = ['172.17.0.3','172.17.0.5']
env.hosts = ['ip_addr:22923']
env.user='user_here'
env.password='passwdord_here'
env.warn_only = True


def install_nginx():
        run('apt-get install nginx -y')
def start_nginx():
        run('/etc/init.d/nginx start')
def autostart_nginx():
        run('update-rc.d   nginx defaults')
        run('systemctl enabled nginx')
        run('chkconfig nginx on')
def nginx_configs():
        put('/opt/testsite.conf', '/etc/nginx/sites-available/testsite.conf')
        run('ln -s /etc/nginx/sites-available/testsite.conf /etc/nginx/sites-enabled/testsite.conf')
def allow_http_port():
        run('iptables -I  INPUT 1  -p tcp -m tcp -m state --state NEW --dport 80 -j ACCEPT')

def demo():
        run("echo export vi='vim' >> /root/.bashrc")
        global data
        data = run('netstat -ntlp')
#       put('/root/.bashrc','/root/.bashrc')
        return data
def new():
        put('/etc/hosts', '/tmp/hosts')
        put('/etc/resolv.conf', '/tmp/resolv.conf')
        put('/etc/nsswitch.conf', '/tmp/nsswitch.conf')

def install():
        run('apt-get install telnet -y')


tasks.execute(install_nginx)
tasks.execute(start_nginx)
tasks.execute(autostart_nginx)
tasks.execute(nginx_configs)
tasks.execute(allow_http_port)

