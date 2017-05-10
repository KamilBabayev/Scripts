#!/usr/bin/env python3
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

wifipass = ''
for i in range(10):
     wifipass = wifipass + str(randint(0,9))
print(wifipass)


firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
#firefoxProfile.set_preference('permissions.default.image', 2)
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
firefoxProfile.set_preference("http.response.timeout", 10)
firefoxProfile.set_preference("dom.max_script_run_time", 10)
driver = webdriver.Firefox()
driver.get("https://unify_controller_ip:8443")
time.sleep(1)
username=driver.find_element_by_name("username")
username.send_keys("controller_username")
time.sleep(1)
password=driver.find_element_by_name("password")
password.send_keys("controller_password")
time.sleep(1)
login=driver.find_element_by_id("loginButton")
login.click()
time.sleep(3)
driver.get("https://unify_controller_ip:8443/manage/site/default/settings/wlans/54b75bc696959d36eb66c26b/edit/54f586730cf20b39f93a0953")
time.sleep(2)
key = driver.find_element_by_name("wirelessNetworkWpaPskKey")
time.sleep(1)
key.clear()
time.sleep(1)
#key.send_keys("8760251372")
key.send_keys(wifipass)
time.sleep(1)
save=driver.find_element_by_class_name("busyToggle__body")
time.sleep(1)
save.click()
time.sleep(2)
menu = driver.find_element_by_css_selector("div.appOrgSwitcher:nth-child(1) > div:nth-child(1) > span:nth-child(3)")
menu.click()
time.sleep(1)
submenu = driver.find_element_by_css_selector("div.appOrgSwitcher:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > \
li:nth-child(1) > a:nth-child(3) > span:nth-child(2)")
submenu.click()
time.sleep(1)
driver.close()



aduser = 'domain\ad_user'
adpass = 'ad_pass'
FROM = 'fname.sname@domain.az'
TO = ['useruser@mail.ru']
SUBJECT = 'WIFI PASSWORD'
TEXT = 'wifi password:   {}'.format(wifipass)
mailserver = 'mail.domain.az'

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

conn = smtplib.SMTP(mailserver, 587)
conn.starttls()
conn.login(aduser, adpass)
conn.sendmail(FROM,TO,message)

