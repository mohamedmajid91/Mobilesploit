# Version: "v1"
# Description: "Testing Phase"
# Packages: 1
# File: "packages.zip"

import os, sys, requests, time, random, zipfile, urllib, shutil

def extract_update(update):
	zip_ref = zipfile.ZipFile(update, "r")
	zip_ref.extractall("./")
	zip_ref.close()
	os.remove("temp.zip")
	os.remove("packages.zip")
	for _ in os.listdir("./packages"):
		if _ in os.listdir("./exploits"):
			u = open("packages/"+_).read()
			f = open("exploits/"+_,"w")
			f.write(u)
			f.close()
		else:
			shutil.move("packages/"+_,"./exploits")
	shutil.rmtree("./packages")
	

def download(filename):
	updater = urllib.FancyURLopener()
	updater.retrieve("https://raw.githubusercontent.com/RussianOtter/Mobilesploit/master/packages.zip","packages.zip")

def mobileupdate(rate=0.0061,val="",v="",d="", install=""):
	lchr = u"\u2588"
	if raw_input("Mobilesploit Update Available!\nWould you like to update [y/n] ") == "y":
		print "Retrieving Mobilesploit Update..."
		download(install)
		time.sleep(2)
		print "Version:",v
		time.sleep(1)
		print "Description:",d
		time.sleep(1)
		print "Installing Packages..."
		time.sleep(2)
		for pro in range(1,val+1):
			for _ in range(101):
				a = int((_/350.0)*100)
				p = 28-a
				msg = (lchr*a)+(" "*p)+" [%d/%d]  "
				sys.stdout.write("\r"+msg%(pro,val))
				time.sleep(rate)
				if random.randint(0,17) == 1:
					time.sleep(rate*random.randint(8,18))
		extract_update(install)
		time.sleep(0.5)
		print "\nMobilesploit Update Complete!\n"

default = open("try.py").read()

updateurl = "https://raw.githubusercontent.com/RussianOtter/Mobilesploit/master/update.ms"

for _ in range(1):
	try:
		stat = open("update.ms").read()
	except Exception as e:
		if "Mobilesploit.py" not in os.listdir("./"):
			f = open("update.ms","a")
			f.write(default)
			f.close()
			stat = open("update.ms").read()
		else:
			print
			print "[-] Wrong File Location"
			print e
			print
			break
	
	try:
		update = requests.get(updateurl).text
	except Exception as e:
		print
		print "[-] Offline"
		print e
		print
		break
	
	if stat != update:
		packages = update.split("\n")[2].replace("# ","").replace(":","=")
		version = update.split("\n")[0].replace("# ","").replace(":","=")
		description = update.split("\n")[1].replace("# ","").replace(":","=")
		packagefile = update.split("\n")[3].replace("# ","").replace(":","=")
		exec packages
		exec version
		exec description
		exec packagefile
		mobileupdate(val=Packages, d=Description, v=Version, install=File)
