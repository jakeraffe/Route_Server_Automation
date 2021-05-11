import getpass
import telnetlib
import csv
import time

# HOST will change depending on the route server you want to connect to. In this case it is AT&T
HOST = "route-server.ip.att.net"
print("Connecting to ", HOST)

# setting up an instance of the telnet connection socket
tn = telnetlib.Telnet(HOST) 
print("Connection to", HOST, "established")

# Username and password may also be different for other route servers which is why an input is required.
#   However, the variables can be had coded. Usually username and password will be "rviews"
user = input("Login: ")
password = getpass.getpass()

tn.read_until(b"login:")
tn.write(user.encode('ascii') + b"\n")

# Logging into router. The router password may be different
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")

# Open csv file and read comma delimited ip addresses
with open('ip.csv', newline='') as csvfile:
    ip_csv_reader = csv.reader(csvfile, delimiter=',')
    
    # delcare lists.
    ip_list_unjoined = []
    final_var = ""
    
    # iterate through csv ips to build a list in format ['index1', 'index2'...]
    for row in ip_csv_reader:
        ip_list_unjoined = row
    
    # print("IP LIST: ", ip_list,"\n")
    
    i=0
    while i < len(ip_list_unjoined):
        final_var = "show route detail active-path " + ip_list_unjoined[i] + " | match \"AS\""
        tn.write(final_var.encode('ascii') + b"\n")
        time.sleep(1)
        print(i, final_var)
        i += 1
        
tn.write(b"exit\n")
# End looping through ips and exit the router

# Output of commands placed in a variable to be printed later
readAll = tn.read_all().decode('ascii')

# place the output into a variable and send it to a log file
with open('output.txt', "a") as f:
    f.write(readAll)

print(readAll)
# error checking

input("waiting to close...")