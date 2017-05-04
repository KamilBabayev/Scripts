#!/usr/bin/python
# This script checks disks status via smartclt
# if finds error sends mail.  I have used it in hetzner servers.
import re
import subprocess
import smtplib

def send_mail():
    user = 'smtprelay01'
    pwd = 'Smpryyle333@'
    FROM = 'sales@galaxy.az'
    TO = ['kamil.babayev@atltech.az']
    SUBJECT = 'Attention: Galaxy Server Disk status'
    TEXT = 'Please check disk status on server, some problems detected'

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("mail.atl.az", 25)
        server.set_debuglevel(1)
        server.ehlo('mail.atl.az')
        server.esmtp_features['auth'] = 'LOGIN'
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'Successfully sent the mail'
    except:
        print 'Failed to send mail'

disks = [4,5,6,7]
for N in disks:
    megaraid = "megaraid," + str(N)
    p=subprocess.Popen(["smartctl",  "-a", "-d", megaraid,  "/dev/sda", "-H"], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    result = re.findall(r'SMART overall-health\s\S+\s\S+\s\S+\s\S+', output)
    status = str(result).split(':')
    status =  status[1].rstrip("']").lstrip(' ')
    if status != "PASSED":
        send_mail()

