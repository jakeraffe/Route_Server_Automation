import csv

with open('ip.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    ip_list = []
    final_var = ""
    
    for row in spamreader:
        ip_list = row
    
    print("IP LIST: ", ip_list,"\n")
    
    i=0
    while i < len(ip_list):
        final_var = "show route " + ip_list[i] + "| match \"AS path\""
        print(final_var)
        i += 1
        # print("show route " + "\n".join(row) + " | match \"AS path \" ")
# file = open("ip.csv", "r")

# for ips in file.readlines():
#     value = ips.split(",")
#     print("show route", value[0], "| match \"AS path\" \n")