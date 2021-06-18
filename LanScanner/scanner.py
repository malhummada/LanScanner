 
import socket
 
import sys

import inquirer

result = str(2000)

from pprint import pprint
import inquirer

import pyfiglet

 
# ------------------------------- a2 -----------------------------------

def scanips():

    print('\n Enter Network address EX: 192.168.1.0 \n ')

    netadd = str(12)

    netadd = input('Net addr# ')

    r0 = netadd.split('.')[0]
    r1 = netadd.split('.')[1]
    r2 = netadd.split('.')[2]
    r3 = netadd.split('.')[3]

    print('\n Enter port number: ')
    port= int(input('#  '))
    print("\n Please wait... \n")

    for i in range(1,254):
        try:
            sok = socket.socket()
            # sok.connect(r0 + '.' + r1 + '.' + r2 + '.' + i ,80)
            sok.connect((r0 + '.' + r1 + '.' + r2 + '.'+ str(i),port))
            re = str(socket.gethostbyaddr(r0 + '.' + r1 + '.' + r2 + '.'+ str(i)))
            re = re.replace('[','')
            re = re.replace(']','')
            re = re.replace(',','')
            
            print('[+] IP found (' + r0 + '.' + r1 + '.' + r2 + '.'+ str(i) +') '+ str(re))  
            sok.close()
            result = str(result) + str('[+] IP found ' + r0 + '.' + r1 + '.' + r2 + '.'+ str(i)+ '\n') 

        except:

            pass
 

# ---------------------------  a1 ---------------------------------------

def ScanAllforIP(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scanip_port(target,port)


def scanip_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
        
		sock.close()
	except:
		pass


# ----------------------- a3 -------------------------------------------

def ScanSpecialPort(target, port):
	print('\n' + ' Starting Scan For ' + str(socket.gethostbyaddr(target)))
 
	try:
		sock = socket.socket()
		sock.connect((target, port))
		print("[+] Port Opened " + str(port))
        
		sock.close()
        
	except:
		pass
        #  sys.stdout.write(str(port) +", ")
        #  sys.stdout.flush()

# ------------------------------------------------------------------


def ScanAllipsForAllPorts():

    print('\n Enter Network address EX: 192.168.1.0 \n ')

    netadd = str(12)

    netadd = input('Net addr# ')

    r0 = netadd.split('.')[0]
    r1 = netadd.split('.')[1]
    r2 = netadd.split('.')[2]
    r3 = netadd.split('.')[3]



    # print('\n Enter port number: ')
    # port= int(input('#  '))







    print("\n Please wait... \n")

    for i in range(1,254):

        for port in range(1,65535):
             try:
                 sok = socket.socket()
                 # sok.connect(r0 + '.' + r1 + '.' + r2 + '.' + i ,80)
                 sok.connect((r0 + '.' + r1 + '.' + r2 + '.'+ str(i),port))
                 re = str(socket.gethostbyaddr(r0 + '.' + r1 + '.' + r2 + '.'+ str(i)))
                 re = re.replace('[','')
                 re = re.replace(']','')
                 re = re.replace(',','')

                 print('[+] IP found (' + r0 + '.' + r1 + '.' + r2 + '.'+ str(i) +' ) '+ str(re) + '  Port: ' + str(port))  
                 sok.close()
                 result = str(result) + str('[+] IP found ' + r0 + '.' + r1 + '.' + r2 + '.'+ str(i)+ '  Port: ' + str(port) + '\n') 

             except:
             
                 pass







  












result = pyfiglet.figlet_format(" PLEASE USE THIS TOOLS FOR GOODNESS ")
print(result)

 


hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("\n Your Computer Name is: " + hostname )    
print("\n Your Computer IP Address is: " + IPAddr + '\n \n') 


a2=  'Scan all port for special IP (Takes few minutes)'
a3 = 'Scan special port for all devices in local network (Not quick)'
a4 = 'Scan special port for special device IP (Quick)'
a5 = 'Scan for ALL ports for ALL devices in local network (Takes long time)'

questions = [
    inquirer.List(
        "number",
        message="Select one #  ",
        choices=[ a2, a3, a4, a5],
    ),
]

answers = inquirer.prompt(questions)['number']
# print(answers)






if  str(a2) in answers:
  
    targets = input("[*] Enter Targets To Scan(split them by ,): ")
    ports = int('65535')
    if ',' in targets:
    	print(("[*] Scanning Multiple Targets"), 'green')
    	for ip_addr in targets.split(','):
    		ScanAllforIP(ip_addr.strip(' '), ports)
    else:
    	ScanAllforIP(targets,ports)





if  str(a3) in answers:
    scanips()








if  str(a4) in answers:
  
    targets = input("[*] Enter Targets To Scan(split them by ,): ")
    ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
    if ',' in targets:
    	print(("[*] Scanning Multiple Targets"), 'green')
    	for ip_addr in targets.split(','):
    		ScanSpecialPort(ip_addr.strip(' '), ports)
    else:
    	ScanSpecialPort(targets,ports)


if  str(a5) in answers:
   ScanAllipsForAllPorts()

