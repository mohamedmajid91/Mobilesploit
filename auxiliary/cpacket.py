import sys, time, random, os

def loading(rate=0.0007):
	lchr = u"\u2588"
	print "Loading..."
	for _ in range(101):
		a = int((_/1000.0)*100)
		p = 10-a
		msg = (lchr*a)+(" "*p)+" %s"
		_ = str(_)+"%"
		sys.stdout.write("\r"+msg%_)
		time.sleep(rate)
		if random.randint(0,17) == 1:
			time.sleep(rate*random.randint(8,18))
	time.sleep(rate*100)
	print

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

def packet_creation():
	title = "Packet Creation"
	print
	print "="*len(title)
	print title
	print "="*len(title)
	print
	t = raw_input("HTTP/UPnP/BO/MC > ")
	while 1:
		if t.lower() == "http":
			loading(0.007)
			print
			http_req = raw_input("GET/POST > ").upper() + " "
			http_req += raw_input("Path > ") + " HTTP/"
			http_req += raw_input("Version (1.1) > ")+"\r\n"
			if raw_input("Host [y/n] ").lower() == "y":
				http_req += "Host: "+raw_input(" > ") + "\r\n"
			if raw_input("Connection Type [y/n] ").lower() == "y":
				http_req += "Connection: " + raw_input(" > ") + "\r\n"
			if raw_input("Device [y/n] ").lower() == "y":
				http_req += "Device: " + raw_input(" >") + "\r\n"
			if raw_input("Cookie [y/n] ").lower() == "y":
				http_req += "Set-Cookie: " + raw_input(" > ") + "\r\n"
			if raw_input("Content Type [y/n] ").lower() == "y":
				http_req += "Content-Type: " + raw_input(" > ") + "\r\n"
			if raw_input("ETag [y/n] ").lower() == "y":
				http_req += "ETag: " + raw_input(" > ") + "\r\n"
			if raw_input("Custom [y/n] ").lower() == "y":
				print "\nEnter Empty Value To Exit"
				print "\nExample:\nTag: Value\n"
				while 1:
					v = raw_input("Custom > ")
					if len(v) == 0:
						break
					http_req += v + "\r\n"
			if not raw_input("RUDY [y/n] ").lower() == "y":
				http_req += "\r\n"
			print "\nPacket:\n"
			print http_req.replace("\r\n","\\r\\n\n")
			if raw_input("Correct Packet [y/n] ") == "y":
				break
		if t.lower() == "upnp":
			loading(0.007)
			print
			upnp_req = raw_input("M-SEARCH/NOTIFY > ").upper() + " "
			upnp_req += raw_input("URI (*) > ") + " HTTP/"
			upnp_req += raw_input("Version (1.1) > ") + "\r\n"
			if raw_input("Host [y/n] ") == "y":
				upnp_req += "Host: " + raw_input(" > ") + ":" + raw_input("Port (1900) > ") + "\r\n"
			else:
				upnp_req += "Host: 239.255.255.250:1900\r\n"
			if raw_input("SSDP [y/n] ") == "y":
				upnp_req += "MAN: "+ '"ssdp:'+raw_input(" > ")+'"' + "\r\n"
			else:
				upnp_req += 'MAN: "ssdp:discover"\r\n'
			if raw_input("MX [y/n] ") == "y":
				upnp_req += "MX: " + raw_input(" > ") + "\r\n"
			else:
				upnp_req += "MX: 30\r\n"
			if raw_input("ST [y/n] ") == "y":
				upnp_req += "ST: " + raw_input(" > ") + "\r\n"
			else:
				upnp_req += "ST: ssdp:all\r\n"
			if raw_input("TTL [y/n] ") == "y":
				upnp_req += "CACHE-CONTROL: max-age=" + raw_input(" > ") + "\r\n"
			if raw_input("Custom [y/n] ").lower() == "y":
				print "\nEnter Empty Value To Exit"
				print "\nExample:\nTag: Value\n"
				while 1:
					v = raw_input("Custom > ")
					if len(v) == 0:
						break
					upnp_req += v + "\r\n"
			if not raw_input("RUDY [y/n] ").lower() == "y":
				upnp_req += "\r\n"
			print "\nPacket:\n"
			print upnp_req.replace("\r\n","\\r\\n\n")
			if raw_input("Correct Packet [y/n] ") == "y":
				break
		if t.lower() == "mc":
			loading(0.0007)
			print
			mc_title = raw_input("Title: ")
			mc_desc = raw_input("Port: ")
			mc_req = "[MOTD]%s[/MOTD][AD]%s" %(mc_title,mc_desc)
			if not raw_input("RUDY [y/n]") == "y":
				mc_req += "[/AD]"
			print "\nPacket:"
			print mc_req
			if raw_input("\nCorrect Packet [y/n] ") == "y":
				break
		if t.lower() == "bo":
			loading(0.0007)
			print
			buf_pat = raw_input("Buffer Overflow Pattern > ")
			buf_len = input("Buffer Length > ")
			shellcode = ""
			print "Shellcode"
			while 1:
				s = raw_input(" > ")
				if len(s) == 0:
					break
				shellcode += s.replace("	","\t") + "\r\n"
			buf_payload = (buf_pat*buf_len)[:buf_len] + shellcode
			print "\nPayload Statistics\n"
			print "Shellcode Length:",len(shellcode)
			print "Buffer Length",len(buf_payload)-len(shellcode)
			print "Total Length",len(buf_payload)
			if raw_input("\nCorrect Packet [y/n] ") == "y":
				break
		else:
			print "\nInvalid Input\n"
			t = raw_input("HTTP/UPnP/BO/MC > ")
			
	pf = "../payload/"
	if raw_input("Save Payload [y/n] ") == "y":
		if "payload" in os.listdir("./"):
			pf = "./payload/"
		pn = raw_input("Filename >")
		pf += pn
		if t.lower() == "http":
			payload = http_req
			loading(0.0007)
		if t.lower() == "upnp":
			payload = upnp_req
			loading(0.0007)
		if t.lower() == "bo":
			buf_payload
			loading(0.00007)
		if t.lower() == "mc":
			mc_req
			loading(0.00007)
		f = open(pf,"a")
		f.write(payload)
		f.close()
		print "Payload Saved!"
	print

try:
	if desc == "get-id":
		print auto_help("cpacket","Normal","Packet Creation")
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

def show_opt():
	print "\nModule Options (axuiliary/cpacket)\n"
	print "  Name     Current Setting  Required  Description"
	print "  ----     ---------------  --------  -----------"
	print "  No Arguments Required\n"

try:
	if desc == "get-opt":
		show_opt()
except:
	pass

try:
	if desc == "proc":
		try:
			packet_creation()
		except Exception as e:
			print "[*] Error While Starting"
			print e
			print
			time.sleep(0.3)
except:
	pass

try:
	if desc == "get-info":
		auto_info(name,"axuiliary/cpacket","Python 2.7","No","N/A","Normal","11/19/17","Russian Otter")
		show_opt()
		targets = {"1":"HTTP","2":"UPnP", "3":"Buffer Overflow","4":"Minecraft :/","5":"Old Routers","6":"Old Computers","7":"FTP Servers"}
		auto_targ(targets)
except:
	pass
