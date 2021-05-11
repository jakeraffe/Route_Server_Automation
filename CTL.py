import getpass
import telnetlib
import csv
import time
import re

cidr_dir = {'/24': '255.255.255.0', '/25': '255.255.255.128', '/26': '255.255.255.192',
            '/27': '255.255.255.224', '/28': '255.255.255.240', '/29': '255.255.255.248',
            '30': '255.255.255.252', '/31': '255.255.255.254', '/32': '255.255.255.255'}


# HOST will change depending on the route server you want to connect to. In this case it is AT&T
HOST = "route-server.eu.gblx.net"

# Username and password may also be different for other route servers which is why an input is required.
#   However, the variables can be had coded. Usually username and password will be "rviews"
# user = input("Login: ")
# password = getpass.getpass()

# setting up an instance of the telnet connection socket
tn = telnetlib.Telnet(HOST) 

# tn.read_until(b"login:")
# tn.write(user.encode('ascii') + b"\n")

# # Logging into router. The router password may be different
# if password:
#     tn.read_until(b"Password:")
#     tn.write(password.encode('ascii') + b"\n")

# # Open csv file and read comma delimited ip addresses
# with open('ip.csv', newline='') as csvfile:
#     ip_csv_reader = csv.reader(csvfile, delimiter=',')
    
#     # delcare lists.
#     ip_list_unjoined = []
#     final_var = ""
#     # iterate through csv ips to build a list in format ['index1', 'index2'...]
#     for row in ip_csv_reader:
#         ip_list_unjoined = row
    
#     print("IP LIST: ", ip_list,"\n")
    
#     i=0
#     while i < len(ip_list_unjoined):
#         # we are taking out the cidr and doing a subnet lookup based on its cidr value
#         print('Prefix Given:', ip_list_unjoined[i])
#         prefix = ip_list_unjoined[i]
#         # getting the cidr or /value
#         cidr_extract = re.findall("/\d{2}", prefix)
        
#         # since we get a list from the line above and we want a string
#         cidr_extract = cidr_extract[0]
#         # getting subnet mask by doing a lookup
#         subnet_mask = cidr_dir[cidr_extract]
        
#         # split ip from its existing cidr value
#         non_cidr_ip = prefix.split(cidr_extract)
#         non_cidr_ip = non_cidr_ip[0]
        
#         joined_ip = non_cidr_ip + " " + subnet_mask
        
#         final_var = "show ip bgp " + joined_ip + " | match \"AS\""
#         tn.write(final_var.encode('ascii') + b"\n")
#         time.sleep(1)
#         print(i, final_var)
#         i += 1

tn.write(b"show ip bgp 8.45.145.0/24")
        
tn.write(b"exit\n")
# End looping through ips and exit the router

# place the output into a variable and send it to a log file
readAll = tn.read_all().decode('ascii')
with open('output.txt', "a") as f:
    f.write(readAll)

print(readAll)
# error checking