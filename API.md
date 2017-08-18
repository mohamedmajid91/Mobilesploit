**Mobilesploit Exploit API**

Every Mobilesploit exploit, payload, or auxiliary has the basic API script included!

The API allows `Mobilesploit.py` to get information on all the different exploits! All the API code it put at the beginning of the exploit!


Example of Mobilesploit API
===========================

*Printing Information*

This first section of the API defines the functions that allow Mobilesploit to print it's information in an organized fasion.

```python
import time

def auto_help(name,rank,description):
	stbl = "  " + name + " "*(13-len(name)+4) + rank + " "*(8-len(rank)+4) + description
	return stbl

def auto_opt(name,cset,req,description):
	stbl = "  " + name + " "*(9-len(name)) + cset + " "*(15-len(cset)+2) + req + " "*(8-len(req)+2) + description
	print stbl

def auto_targ(targetlist):
	print "Vulnrable Applications (%s)\n" %name
	print "  ID       Device"
	print "  --       ------"
	for _ in targetlist:
		print "  "+_+" "*(9-len(_))+targetlist[_]
	print

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
```

*Responding To Information Requests*

This next portion of code is used to respond to Mobilesploit's Command: `show exploits`. When Mobilesploit gets that command it will run all programs in the `exploit`, `auxiliary`, and `payload` folders, while setting the local variable `desc` to `"get-id"`!

```python
try:
	if desc == "get-id":
		print auto_help("Temporary","WeakAF","Just A Test")
except:
	pass
```

*Setting Values and Requirements*

The first section that contains lots of `try:` and `except:` is used to define premade variables!

When you try a variable it will check if it is defined, so if the variable isnt defined then it will fail. When this fails `except` is used to define it, if it has a default value (while at the same time preventing changes to custom variables)!

This part of this code is used to check/respond to `Mobilesploit` and tell the program what variables have been set and which variables are needed! And the last part checks `desc` to see if the program is being called to show options!

```python
try: BUF
except: BUF = 1024
try: RPORT
except: RPORT = 23
try: TIMEOUT
except: TIMEOUT = 5

def show_opt():
	print "\nModule Options (exploits/BufferOverflow)\n"
	print "  Name     Current Setting  Required  Description"
	print "  ----     ---------------  --------  -----------"
	try:
		auto_opt("BUF",str(BUF),"no","Buffer Size")
	except:
		auto_opt("BUF","  ","no","Total Buffer Size")
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
	if desc == "get-opt":
		show_opt()
except:
	pass
```

*Information Response*

When Mobilesploit asks an exploit for it's information, this part of code establishes the response with the information needed!

```python
try:
	if desc == "get-info":
		auto_info(name,"exploit/BufferOverflow","Python 2.7","No","IDGAF License","Normal")
		show_opt()
		targets = {"1":"PacMan SSH","2":"Simple Socket Servers"}
		auto_targ(targets)
except:
	pass
```

*Running The Exploit*

And this final part defines your exploit and includes the code that checks if `desc` wants to execute your exploit!

_The exploit will not run if the needed variables are unset!_

```python
def BufferOverflow():
	"Exploit code goes here"
	pass

try:
	if desc == "proc":
		try:
			if not RHOST and not RPORT and not TIMEOUT and not BUF:
				print "Options Still Unset"
			else:
				bufferoverflow(RHOST,BUF,RPORT, TIMEOUT)
		except:
			time.sleep(0.3)
			show_opt()
except:
	pass
```
