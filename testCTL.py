import telnetlib
import time

# HOST will change depending on the route server you want to connect to. In this case it is AT&T
HOST = "route-server.ip.att.net"
tn = telnetlib.Telnet(HOST) 
time.sleep(2)
# The private IP below is a just a placeholder. Replace with a known public IP address to test.
tn.write(b"show ip bgp 192.168.1.0/24")
time.sleep(2)
tn.write(b"exit\n")

readAll = tn.read_all().decode('ascii')
print(readAll)