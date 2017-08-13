import getpass
import sys
import telnetlib


HOST = "10.95.50.3"
user = raw_input("username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST,"23")
tn.read_until("Username: ",5)
tn.write(user + "\r\n")

tn.read_until("Password: ")
tn.write(password + "\r\n")


tn.write("conf t\n")
for n in range(5,6):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name python_vlan_" + str(n) + "\n")












