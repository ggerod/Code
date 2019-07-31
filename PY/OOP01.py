#!/usr/local/bin/python3

class gradeset:
#	def __init__(self,grades):
#		self.grades=grades
	def setGrades(self,grades):
		self.grades=grades

	def setID(self,id):
		self.id=id

	def setName(self,studentname):
		self.name=studentname

	def average(self):
		return (sum(self.grades)/len(self.grades))

	def displaygrades(self):
		print(self.grades)
	
	def getName(self):
		return self.name

	def getID(self):
		return self.id

grades1=[1,2,3,4]
grades2=[4,36,76,3]
grades3=[100]

g1 = gradeset()
g2 = gradeset()
g3 = gradeset()

print("type of g1 = ",type(g1))

g1.setGrades(grades1)
g1.setID(123)
g1.setName("Joe Blow")


g1.displaygrades()
print(g1.average())
print("student name is: ",g1.getName())
print("student id is: ",g1.getID())
