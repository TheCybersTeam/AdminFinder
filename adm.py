# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# Version: Beta 0.2

import urllib as cybers

url = "http://target.com.br/"
directories = ["adm", "painel", "administrador", "login", "admin"]

for i in directories:
	target = url + i
	res = cybers.urlopen(target)

	if res.getcode() == 200:
		print "[+] " + target 
	else:
		print "[-] " + target
