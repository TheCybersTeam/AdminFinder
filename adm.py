# Facebook: https://www.facebook.com/TheCybersTeam
# Group: 	https://www.facebook.com/groups/TheCybersTeam
# Channel:  https://www.youtube.com/channel/UCKFMv1cifW55lKKps2thhbw
# Version: Beta 0.1

import urllib as cybers

url = "http://www.target.com.br/admin"
res = cybers.urlopen(url)

if res.getcode() == 200:
	print "Found!"
else:
	print "Not found!"