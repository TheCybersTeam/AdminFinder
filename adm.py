# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# Version: Beta 0.3

import urllib as cybers
import subprocess as sp
import sys
sp.call('cls',shell=True)
header="""
____ _              ___      _                     _____                      
/__   \ |__   ___    / __\   _| |__   ___ _ __ ___  /__   \___  __ _ _ __ ___  
  / /\/ '_ \ / _ \  / / | | | | '_ \ / _ \ '__/ __|   / /\/ _ \/ _` | '_ ` _ \ 
 / /  | | | |  __/ / /__| |_| | |_) |  __/ |  \__ \  / / |  __/ (_| | | | | | |
 \/   |_| |_|\___| \____/\__, |_.__/ \___|_|  |___/  \/   \___|\__,_|_| |_| |_|
                         |___/                                                 

More: https://www.facebook.com/TheCybersTeam
Fast and easy admin finder hack tool Beta 0.3
"""
print header

wordlist = open('wordlist.txt', 'r')

fail = "Fail, try it: \npython admin.py http://www.yourtarget.com.br"

try:
	url = sys.argv[1]
except:
	print fail
	exit()

try:
	cybers.urlopen(url)
	print "\nConection OK!"
	print "Initializing the search...\n"
except:
	print fail
	exit()
		
for i in wordlist:
	target = url + "/" + i
	res = cybers.urlopen(target)

	if res.getcode() == 200:
		print "[+] " + target
	else:
		print "[-] " + target