import os
from datetime import datetime
import csv

dtnow = datetime.now().strftime('%d%m%Y%H%M%S')
print('Please enter IP Block (x.x.x.)')
ipblock = input('IP Block: ')
print('Enter range of IPs:')
xfirst = int(input('From: '))
xlast = int(input('To: '))
print('-'*60)
iplist = [] #declare ip list
#len(iplist)    #verify empty list

with open(f'pingresults_{dtnow}.csv','w') as output:
    fieldnames = ['IP Address','Status']   #create field names/header of the table
    ipwrite = csv.DictWriter(output, fieldnames = fieldnames, delimiter = ',')    #write csv file with new delimiter
    ipwrite.writeheader()

    for ip in range(xfirst,(xlast + 1)):
        iplist.append(ipblock +str(ip))    #generate ip block

    #print(len(iplist)) #verify length of ip block
    #print(iplist)

    for ip in iplist:
        #print(ip)
        print('ping ' + ip)
        response = os.popen('ping ' + ip).read()
        print(response)

        if "(100% loss)"  in response:
            print("DOWN " + ip + " Ping Failed")
            ipwrite.writerow({'IP Address':ip,'Status':'DOWN'})
        else:
            print("UP " + ip + " Ping Successful")
            ipwrite.writerow({'IP Address':ip,'Status':'UP'})
