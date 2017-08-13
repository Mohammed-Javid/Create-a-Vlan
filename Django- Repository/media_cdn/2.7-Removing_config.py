import getpass
import sys
import telnetlib


HOST = "172.31.193.37"
user = raw_input("username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST,"23")
tn.read_until("Username: ",5)
tn.write(user + "\r\n")

tn.read_until("Password: ")
tn.write(password + "\r\n")

tn.write("conf t\r\n")
tn.write("no int loop 1\r\n")
tn.write("no ip address 2.2.2.2 255.255.255.255\r\n")








