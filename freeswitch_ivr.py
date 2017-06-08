#!/usr/bin/python

import freeswitch
from freeswitch import *
import os, time
sounds_dir='/usr/share/freeswitch/sounds/en/us/callie/ivr/8000/'
internal_nums = ['1000','1001','1002','1003','1004','1005', '1006', '1007','1008','1009','1010']

def handler(session, args):
    session.answer()
    session.streamFile(sounds_dir + "boawelcome.wav")
    #session.sleep(3000)
    #while session.ready() == True:
    digits = session.getDigits(4, "", 5000)
    #digits = session.getDigits(4, "", 5000)
    #session.sleep(3000)
    freeswitch.consoleLog('alert', digits)
    if session.getVariable("callee_id_name") == '1003':
        freeswitch.consoleLog('alert', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    if not digits:
        #session.streamFile(sounds_dir + "boa_yonlendir.wav")
        session.streamFile(sounds_dir + "nomre_yonlendir.wav")
        session.execute("execute_extension", "1002 XML default")
    if digits:
        #for i in internal_nums:
        #if digits not in internal_nums:
        count = 0
        while digits not in internal_nums:
        #freeswitch.consoleLog('info', "Such number does not exist: " +  digits)
            session.streamFile(sounds_dir + "nomre_yalnish.wav")
            digits = session.getDigits(4, "", 5000)
            if digits in internal_nums:
                session.execute("execute_extension", digits + " XML default")
            count +=1
            if count == 2:
                session.streamFile(sounds_dir + "nomre_yalnish.wav")
                session.hangup()
                break
            #session.hangup()
        else:
            session.execute("execute_extension", digits + " XML default")

