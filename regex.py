import re

cidr_dir = {'/20': '255.255.240.0', '/21': '255.255.248.0', '/22': '255.255.252.0',
            '/23': '255.255.254.0', '/24': '255.255.255.0', '/25': '255.255.255.128', 
            '/26': '255.255.255.192', '/27': '255.255.255.224', '/28': '255.255.255.240',
            '/29': '255.255.255.248', '30': '255.255.255.252', '/31': '255.255.255.254',
            '/32': '255.255.255.255'}


testvar = '198.162.5.0/24'
print('IP address:', testvar)

x = re.findall("/\d{2}",testvar)
print('Printing regex cidr lookup from ip:', x)
x = x[0]
print('Printing subnet from cidr lookup:', cidr_dir[x], '\n')
tempSub = cidr_dir[x]
print(tempSub)
print("Good but original prefix still is in cidr:", testvar, "\n")

print("We need to change that\n")

print(testvar.split(x))
a = testvar.split(x)
a = a[0]
print(a)
print("Now we need to join with octets\n")

joined = a + " " + tempSub
print(joined)

# print(splitString)

