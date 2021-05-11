# Route-Server_Automation
Used to automate the proccess of checking BGP advertisments with carrier route servers

For ip.csv:
input IP addresses in the following format delimited by a ',':  
     192.168.1.0/24,192.144.3.1/24
     The IP addresses above are private IP's and need to be replaced with the public IP addresses that you want to test against the carriers route server  
  
If you want to resuse the code in a .py file for another carrier, you must specify the appropriate route server to log into, for example ATT is "route-server.ip.att.net".  
  
Additionally, each carrier route server has a different login method.  
     For example, the ATT route server requires a username and password so the script asks for the user prompt.  
    


PLEASE BE AWARE:
Many of these route servers use telnet which is an unsecured connection allowing a man-in-the-middle attacker to see all data. Please be cautious when using a telnet connection to transfer protected data. 
