#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

# Or uncomment this same variables assign values and comment below 
# same name variables.
#sender="name@mail.ru"
#password="enter_pass_here"
#to="enter_recipient_here"

sender=input("Enter credentials to auth from smtp server, email: ")
password=getpass()
to=input("Enter recipient email: ")
subject="Welcome"
text = """I am happy to inform you that we have plenty of matter
	  So are you ready to starting working with our company?
	we provide different kind of advantages, thanks a lot !!!"""



msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = to

text = MIMEText(text, 'text')
msg.attach(text)

server=smtplib.SMTP('smtp.mail.ru:587')
server.ehlo()
print("Connected to mail server")
server.starttls()
server.login(sender,password)
print("Successfully authenticated to server")
server.sendmail(sender,to,msg.as_string())
print("mail has been sent")
server.close()
