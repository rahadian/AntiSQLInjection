import time
import os
import sys

#import subprocess
colorred = "\033[01;31m{0}\033[00m"
colorgrn = "\033[01;36m{0}\033[00m"
if not os.geteuid() == 0:
	print colorred.format ("You need root permission to run it !")
	sys.exit()
def opening():
        print colorred.format ("============================")
	print colorgrn.format ("AntiSQLInjection by AryaTUX")
	print colorred.format ("============================")
        print "(1)Execute"
        print "(2)Delete rules"
        print "(3)Log"
	print "(4)Exit"
        choose = raw_input ("What will you do ?")
        choose = int(choose)
        if choose == 1:
                execute()
        elif choose == 2:
                delete()
        elif choose == 3:
		log()
        elif choose == 4:
		print colorred.format("BYE !!!")
                exit()
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
			return opening()
                        #print "DETECTED"
def log():
	def follow2(file):
		#file.seek(0.2)
		while True:
			line2 = file.readline()
			if not line2:
				time.sleep(0.0)
				continue
			yield line2
	logfile = open ("/var/log/kern.log")
	loglines = follow2(logfile)
	for line2 in loglines:
		print line2,
def delete():
        ipdel = raw_input("Enter your network ip(ex:192.168.0.0/24) :")
        dibdel1 = "iptables -D INPUT -p tcp -s {} -m string --string \"%27\" --algo bm -j LOG --log-prefix \"SQL_INJECTION DETECTED \"" .format(ipdel)
	dibdel2 = "iptables -D INPUT -p tcp -s {} -m string --string \"%27\" --algo bm -j REJECT" .format(ipdel)
        os.system (dibdel2)
	os.system (dibdel1)
        print colorred.format ("DELETED !!!")
	opening()
opening()
