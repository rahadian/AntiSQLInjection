import time, os
import sys
import subprocess

if not os.geteuid() == 0:
	sys.exit ("You need root permission to run it !")
os.system ('iptables -A INPUT -p tcp -s 192.168.1.0/24 -m string --string "%27" --algo bm -j LOG --log-prefix "SQL_INJECTION "')
def follow(file):
    file.seek(0,2)      
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
		if "SQL_INJECTION" in line:
			os.system ('iptables -A INPUT -p tcp -s 192.168.1.0/24 -m string --string "%27" --algo bm -j REJECT')
			print "DETECTED"


