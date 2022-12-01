'''
Script : FindMAC
Author : Nikhil Leo
Purpose : To analyze dhcp logs and filter out unique connections to a csv file
Usage : python main.py
Tested : Windows-11 with Python version 3.10
Notes : Script will create a MAC_Details.csv file with mac address,ip,hostname and manufacturer name
'''
# Import modules
import Source.dict as d
import Source.openfile as o
import Source.createcsv as c

# Variables
LOG_FILE = "./dhcpd.log"
MAC_DETAILS = "./MAC_Details.csv"
master_list=[]

# calling fucntions
log_file =o.open_log_file(LOG_FILE)

#file will be checked line by line
for i in log_file:
    #line will be splited for accessing the usefull line.
    dhcp_req=i.split(': ')[1]
    temp_line=dhcp_req.split(' ')
    if temp_line[0]== 'DHCPACK' and temp_line[1]=='on':
        #remove the brackets of the hosts.
        log = [val.strip('(').strip(')') for val in temp_line]
        temp_list=[]
        mac_addr=log[4]
        oui=mac_addr[0:8]
        ip_addr=log[2]
        HOST_NAME=log[5]
        if log[5]=='via':
            HOST_NAME='NO_HOST_NAME_AVAILABLE'
        #pushing the MAC Address, IP Address and Host to the list.
        temp_list.append(mac_addr)
        temp_list.append(ip_addr)
        temp_list.append(HOST_NAME)
        #pushing the Vendor details fechted using find_mac function to the list.
        temp_list.append(d.find_vend(oui))
        if temp_list not in master_list:
            master_list.append(temp_list)
# calling functions
rowheader=[('MAC Address', 'IP Address', 'HOST', 'Vendor')]
finallist= rowheader + master_list
c.create_csv_file(MAC_DETAILS, finallist)
