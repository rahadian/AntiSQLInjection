import time
import os
import sys
#import subprocess

if not os.geteuid() == 0:
        sys.exit ("You need root permission to run it !")
def opening():
        print "===== AntiSQLInjection by AryaTux ====="
        print "(1)Execute"
        print "(2)Delete rules"
        print "(3)Exit"
        choose = raw_input ("What will you do ?")
        choose = int(choose)
        if choose == 1:
                execute()
        elif choose == 2:
                delete()
        elif choose == 3:
                exit()
        else:
                print "Choose the correct number ! "

def execute():
        ipex = raw_input("Enter your network ip(ex:192.168.0.0/24) :")
        dibex = "iptables -A INPUT -p tcp -s {} -m string --string \"%27\" --algo bm -j LOG --log-prefix \"SQL_INJECTION DETECTED \"" .format(ipex)
        dibex2 = "iptables -A INPUT -p tcp -s {} -m string --string \"%27\" --algo bm -j REJECT" .format(ipex)
        os.system (dibex)
        def follow(file):
                file.seek(0,2)      # Go to the end of the file
                while True:
                        line = file.readline()
                        if not line:
                                time.sleep(0.0)
                                continue
                        yield line

        logfile  = open("/var/log/kern.log")
	loglines = follow(logfile)

        for line in loglines:
                print line,
                if "SQL_INJECTION DETECTED " in line:
                        os.system (dibex2)
                        #print "DETECTED"
def delete():
        ipdel = raw_input("Enter your network ip(ex:192.168.0.0/24) :")
        dibdel = "iptables -D INPUT -p tcp -s {} -m string --string \"%27\" --algo bm -j LOG --log-prefix \"SQL_INJECTION DETECTED \"" .format(ipdel)
        os.system (dibdel)
        print "DELETED !"

opening()
