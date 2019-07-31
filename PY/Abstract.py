#!/usr/local/bin/python3
from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
	@abstractmethod
	def scroll(self):
		pass

	@abstractmethod
	def click(self):
		pass


class HP(TouchScreenLaptop):
	def scroll(self):
		print("Hi, I am HP")


class DELL(TouchScreenLaptop):
	def scroll(self):
		print("Hi, I am DELL")


class HPNotebook(HP):
	def click(self):
		print("HP click")


class DELLNotebook(DELL):
	def scroll(self):
		print("DELL scroll")

	def click(self):
		print("DELL click")


nb1 = HPNotebook()
nb2 = DELLNotebook()

nb1.scroll()
nb1.click()
nb2.scroll()
nb2.click()
