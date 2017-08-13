from __future__ import print_function
from netmiko import ConnectHandler
import netmiko
import sys
import time
import select
import paramiko
import re
import datetime
import os



x=datetime.date.today()
date=x.isoformat()

os.mkdir(date)
os.chdir(date)

platform = 'cisco_ios'
username = 'dimension' # edit to reflect
password = 'password' # edit to reflect


ip_add_file = open(r'C:\Users\uiic_mpls_dd\Downloads\IP.txt','r') #   list of IP addresses y to connect through SSH
commands = open(r'C:\Users\uiic_mpls_dd\Downloads\commands.txt','r') # list of commands to be collected

for host in ip_add_file:
    try:
        host = host.strip()
        device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        fd = open(host+'.txt','w') # Where you want the file to save to
        sys.stdout = fd
        output = device.send_command('terminal length 0')
        output = device.send_command('enable') #Editable to be what ever is needed
        for command in commands:
            command = command.strip()            
            output = device.send_command(command)
            print('+++++++++++++' + command + '+++++++++++++++++\n')
            print(output)
        print('##############################################################\n')
        fd.close()
    except Exception as e:
        error = open('error.txt','a+')
        sys.stdout = error
        print(host,e)
        error.close()
        
