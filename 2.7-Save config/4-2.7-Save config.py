
#!/usr/bin/env python

import getpass
import telnetlib

#Ask for username and password
user = raw_input("username: ")
password = getpass.getpass()


#Open a file called myswitches

f = open('myswitches.txt')

#Telnet to switch and get the running config
for line in f:
        print "Get running config from Switch " + (line)
        HOST = line.strip()  
        tn = telnetlib.Telnet(HOST,"23")
        
        tn.read_until("Username: ",5)
        tn.write(user + "\r\n")

        tn.read_until("Password: ")
        tn.write(password + "\r\n")

        tn.write("ter len 0\n")
        tn.write("sh run\n")
        tn.write("exit\n")

        readoutput = tn.read_all()
        saveoutput = open("switch" + HOST,"w")
        saveoutput.write(readoutput)
        saveoutput.close
        









