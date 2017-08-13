"""Script to upgrade a Cisco IOS devices."""
import sys
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler, FileTransfer



def main():
    """Script to upgrade a Cisco IOS devices."""
    ip_addr = input("Enter device IP address: ")
    password = getpass()
    start_time = datetime.now()
    print (">>>> {}".format(start_time))

    net_device = {
        'device_type': 'cisco_ios',
        'ip': ip_addr,
        'username': 'admin',
        'password': password,
        'secret': password,
        'port': 22,
    }

    print ("Logging in to Device")
    ssh_conn = ConnectHandler(**net_device)
    print()

    # ADJUST TO TRANSFER IMAGE FILE
    dest_file_system = input('Enter the file system: ')
    source_file = input('Enter source file name:')
    dest_file = input('Destination file name:')
    #alt_dest_file = 'asa825-59-k8.bin'
    #scp_changed = False

    with FileTransfer(ssh_conn, source_file=source_file, dest_file=dest_file,
                      file_system=dest_file_system) as scp_transfer:

        #if not scp_transfer.check_file_exists():
            #if not scp_transfer.verify_space_available():
                #raise ValueError("Insufficient space available on remote device")

            

            print ("\nTransferring file\n")
            scp_transfer.transfer_file()
            print('file transferred successfully')



        #print "\nVerifying file"
        #if scp_transfer.verify_file():
        #    print "Source and destination MD5 matches"
        #else:
        #    raise ValueError("MD5 failure between source and destination files")

    print ("Sending boot commands")
    full_file_name = "{}{}".format(dest_file_system,dest_file)
    boot_cmd = 'boot system {}'.format(full_file_name)
    output1 = ssh_conn.send_command('conf t')
    output = ssh_conn.send_command(boot_cmd)
    print(output1)
    print(output)

#
    #print "\nVerifying state"
    output = ssh_conn.send_command('show boot')
    print (output)

    # UNCOMMENT TO PERFORM WR MEM AND RELOAD
    #print "\nWrite mem and reload"
    #output = ssh_conn.send_command_expect('write mem')
    #output += ssh_conn.send_command('reload')
    #output += ssh_conn.send_command('y')
    #print output

    print (">>>> {}".format(datetime.now() - start_time))
    print()

if __name__ == "__main__":
    main()
