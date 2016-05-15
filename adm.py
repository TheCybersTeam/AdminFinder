# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# Greatz:   Geolado
# Version:  Beta 0.4

import urllib as cybers
import sys
import os

os.system('cls')
wordlist = open('wordlist.txt', 'r')

def admin_finder(url) :
	try:
		cybers.urlopen(url)
		print "\nConection OK!"
		print "Initializing the search...\n"
	except:
		print "Fail, try it: \npython admin.py http://www.yourtarget.com.br"
		exit()
			
	for i in wordlist:
		target = url + "/" + i
		res = cybers.urlopen(target)
	
		if res.getcode() == 200:
			print "[+] " + target 
		else:
			print "[-] " + target
		
def main() :
	print " _____ _              ___      _                     _____                     "
	print "/__   \ |__   ___    / __\   _| |__   ___ _ __ ___  /__   \___  __ _ _ __ ___  "
	print "  / /\/ '_ \ / _ \  / / | | | | '_ \ / _ \ '__/ __|   / /\/ _ \/ _` | '_ ` _ \ "
	print " / /  | | | |  __/ / /__| |_| | |_) |  __/ |  \__ \  / / |  __/ (_| | | | | | |"
	print " \/   |_| |_|\___| \____/\__, |_.__/ \___|_|  |___/  \/   \___|\__,_|_| |_| |_|"
	print "                         |___/                                                 Beta 0.4"

	user_url = sys.argv[1]
	admin_finder(user_url)

if __name__ == "__main__":
	main()
