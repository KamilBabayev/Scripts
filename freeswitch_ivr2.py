#!/usr/bin/python
import freeswitch
from freeswitch import *
import os, time, subprocess

sounds_dir='/usr/share/freeswitch/sounds/en/us/callie/ivr/8000/'
internal_nums = ['1000','1001','1002','1003','1004','1005', '1006',
                '1007','1008','1009','1010','1011', '1012', '1013',
                '1014','1015','1016','1017','1018', '1019']

def handler(session, args):
    session.answer()
    session.streamFile(sounds_dir + "welcome.wav")
    callee_id_name = session.getVariable("caller_id_name")
    freeswitch.consoleLog('alert', 'Callee_id_name:'+callee_id_name)
    #session.sleep(3000)
    #while session.ready() == True:
    digits = session.getDigits(4, "", 5000)
    #session.sleep(3000)
    freeswitch.consoleLog('alert', digits)
    #contact_available = session.getVariable( "contact_available" )
    #freeswitch.consoleLog('alert', contact_available)

    if session.getVariable("callee_id_name") == '1003':
        freeswitch.consoleLog('alert', 'check')
    if not digits:
        session.streamFile(sounds_dir + "forwarding.wav")
        #session.execute("execute_extension", "1002 XML default")
        session.transfer("1002", "XML", "default")
    if digits:
        #for i in internal_nums:
        #if digits not in internal_nums:
        count = 0
        while digits not in internal_nums:
            if count == 2:
                session.streamFile(sounds_dir + "return_with_correct_ext_number.wav")
                session.hangup()
                break
        #freeswitch.consoleLog('info', "Such number does not exist: " +  digits)
            session.streamFile(sounds_dir + "extension_is_wrong.wav")
            digits = session.getDigits(4, "", 5000)
            if digits in internal_nums:
                #session.execute("execute_extension", digits + " XML default")
                session.transfer(digits, "XML", "default")
            count +=1
            #if count == 3:
            #    session.streamFile(sounds_dir + "return_with_correct_ext_number.wav")
            #    session.hangup()
            #    break
            #session.hangup()
        else:
            #session.execute("execute_extension", digits + " XML default")
            p = subprocess.Popen(['fs_cli','-x', 'sofia_contact '+digits], stdout=subprocess.PIPE)
            out, err = p.communicate()
            agent_status  = out.rstrip('\n')
            freeswitch.consoleLog('info', out)
            freeswitch.consoleLog('alert', 'transfer OUTSIDE  whileeeeeeeeeeeeeeeeeeeeeee')
            if agent_status == 'error/user_not_registered':
                #freeswitch.consoleLog('info', digits + 'daxili reqemli istifadeci yerinde deyil')
                session.streamFile(sounds_dir + "user_can_not_answer_now.wav")
                session.streamFile(sounds_dir + "thanks_for_calling.wav")
                session.hangup()
            session.streamFile(sounds_dir + "forwarding_to_user.wav")
            session.transfer(digits, "XML", "default")


