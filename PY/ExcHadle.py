#!/usr/local/bin/python3

class InvalidPasswordException(Exception):
	def __init__(self,msg):
		self.msg = msg

try:
	pword = input("Enter a password (min length 8 chars): ")
	if (len(pword) < 8):
		raise InvalidPasswordException("Sorry, the password must be at least 8 characters long")
except InvalidPasswordException as obj:
	print(obj)
else:
	print("The password is good and has length: ",len(pword))
