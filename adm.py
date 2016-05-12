# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# Version: Beta 0.3

import urllib as cybers
import sys

print "_____ _              ___      _                     _____                      "
print "/__   \ |__   ___    / __\   _| |__   ___ _ __ ___  /__   \___  __ _ _ __ ___  "
print "  / /\/ '_ \ / _ \  / / | | | | '_ \ / _ \ '__/ __|   / /\/ _ \/ _` | '_ ` _ \ "
print " / /  | | | |  __/ / /__| |_| | |_) |  __/ |  \__ \  / / |  __/ (_| | | | | | |"
print " \/   |_| |_|\___| \____/\__, |_.__/ \___|_|  |___/  \/   \___|\__,_|_| |_| |_|"
print "                         |___/                                                 Beta 0.3"

directories = ["adm", "painel", "administrador", "login", "admin"]

url = sys.argv[1]

try:
	cybers.urlopen(url)
	print "\nConection OK!"
	print "Initializing the search...\n"
except:
	print "Fail, try it: \npython admin.py http://www.yourtarget.com.br"
	exit()
		
for i in directories:
	target = url + "/" + i
	res = cybers.urlopen(target)

	if res.getcode() == 200:
		print "[+] " + target 
	else:
		print "[-] " + target