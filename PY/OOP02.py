#!/usr/local/bin/python3

class Patient:
	def setID(self,id):
		self.id=id

	def setName(self,name):
		self.name=name

	def setSSN(self,ssn):
		self.ssn=ssn

	def getID(self):
		return self.id

	def getName(self):
		return self.name

	def getSSN(self):
		return self.ssn


p1 = Patient()
p1.setID(123)
p1.setName("Joe Blow")
p1.setSSN("123-45-6789")

print("Patient name is: ",p1.getName())
print("Patient ID is: ",p1.getID())
print("Patient SSN is: ",p1.getSSN())
