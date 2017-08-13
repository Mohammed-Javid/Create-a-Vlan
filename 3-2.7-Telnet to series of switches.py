import getpass
import sys
import telnetlib
user = raw_input("username: ")
password = getpass.getpass()
for n in range (72,77):    
        HOST = "172.29.204." + str(n)
        tn = telnetlib.Telnet(HOST,"23")
        
        tn.read_until("Username: ",5)
        tn.write(user + "\r\n")

        tn.read_until("Password: ")
        tn.write(password + "\r\n")

        tn.write("conf t\r\n")
        tn.write("no int loop 1\r\n")
        tn.write("no ip address 2.2.2.2 255.255.255.255\r\n")








