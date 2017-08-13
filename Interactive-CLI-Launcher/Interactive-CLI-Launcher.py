import csv
import os
from tkinter import *
import subprocess
import telnetlib


#Function to ping the ip address of the selected branch
def read_branch_ip_to_ping():
    file = open('branchdetails.csv')
    read = csv.reader(file)
    data = dict(read)
    branch = Name.get()
    address = data[branch]
    os.system('ping {} '.format(address, shell=True))

#Function to SSH the ip address of the selected branch
def get_branch_ip_and_ssh():
    file = open('branchdetails.csv')
    read = csv.reader(file)
    data = dict(read)
    branch = Name.get()
    address = data[branch]
    username = 'cisco'
    ipaddress = address
    password = 'cisco'
    # os.system('plink -ssh {}@{} -pw {}'.format(username, ipaddress, password, shell=True))
    subprocess.Popen("putty.exe -ssh cisco@{}".format(address))

#Function to Telnet the ip address of the selected branch
def get_branch_ip_and_telnet():
    file = open('branchdetails.csv')
    read = csv.reader(file)
    data = dict(read)
    branch = Name.get()
    address = data[branch]
    username = 'cisco'
    ipaddress = address
    password = 'cisco'
    # os.system('plink -ssh {}@{} -pw {}'.format(username, ipaddress, password, shell=True))
    os.system("putty.exe -telnet cisco@{}".format(address))
    #telnet = telnetlib.Telnet(address)
    #telnet.read_until("Username: ")
    #telnet.write(username + "\n")
    #telnet.read_until("Password: ")
    #telnet.write(password + "\n")


#function to read the listbox selection and put the result in an entry widget
def get_list(event):

    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    # delete previous text in enter1
    Name.delete(0, 50)
    # now display the selected text
    Name.insert(0, seltext)

# Function to update the listbox from the file
def update_listbox(*args):
    search_term = search_var.get()
    listbox1.delete(0, END)
    for item in branch_trace:
        if search_term.lower() in item.lower():
            listbox1.insert(END, item)


#Creating Tkinter window for GUI and defining frame parameters
mygui = Tk()
mygui.title("DDIN-NOC-MGMT-TOOL")
mygui.geometry("1500x700+0+0")
frame = Frame(mygui, bg='red')
frame.pack()
mygui.configure(background='green')

#Adding background image
backgroundimage = PhotoImage(file='ddlogo.gif')
backgroundlabel = Label(mygui, image=backgroundimage)
# backgroundlabel.image = backgroundimage
# backgroundlabel.place(x=0,y=0,rely=1, relx=1, anchor=NE)
backgroundlabel.pack(side='bottom', anchor=SE, pady=10, padx=10)


#Adding label in the frame
mylabel1 = Label(text='Powered by', fg='black', bg='green', font='verdana 10 italic bold')
mylabel1.place(x=1255, y=560)

mylabel = Label(text='Enter the Branch Name', fg='black', bg='green', font=' verdana 15 bold')
mylabel.place(x=10, y=5)

branchnames = open('branchdetails.csv')

branchlist = csv.reader(branchnames)

branches = []

for branchname in branchlist:
    branches.append(branchname[0])

# create the listbox (note that size is in characters)
listbox1 = Listbox(mygui, width=51, height=30, font='Helvetica 12', bg='black', fg='white')
listbox1.place(x=10, y=100)

# create a vertical scrollbar to the right of the listbox
yscroll = Scrollbar(command=listbox1.yview, orient=VERTICAL, bg='grey')
yscroll.place(x=456, y=100, height=574)
listbox1.configure(yscrollcommand=yscroll.set)

search_var = StringVar()
search_var.trace('w', update_listbox)

#Create Entry widget to display selected branch
Name = Entry(mygui, width=77, textvariable=search_var, bg='black', fg='white')
Name.place(x=10, y=44)


#Creating buttons
pingbutton = Button(mygui, text='PING', command=read_branch_ip_to_ping, bg='black', fg='white')
pingbutton.place(x=500, y=40)
pingbutton.configure(height=1, width=6)

sshbutton = Button(mygui, text='SSH', command=get_branch_ip_and_ssh, bg='black', fg='white')
sshbutton.place(x=570, y=40)
sshbutton.configure(height=1, width=6)

telnetbutton = Button(mygui, text='TELNET', command=get_branch_ip_and_telnet, bg='black', fg='white')
telnetbutton.place(x=640, y=40)
telnetbutton.configure(height=1, width=6)

for branchname in branches:
    listbox1.insert(END, branchname)

listbox1.bind('<ButtonRelease-1>', get_list)
branch_trace = listbox1.get(0, END)

mygui.mainloop()
