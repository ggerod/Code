#!/usr/local/bin/python3


def dchay(fn):
	def dcfn(nm):
		result = fn(nm)
		result += " how are you"
		return result
	return dcfn


@dchay
def hello(nm):
	return("Hello " + nm)

print(hello("glen"))
