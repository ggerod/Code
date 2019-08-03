#!/usr/bin/python3
from threading import *

def displayodd():
    for n in range(1,101,2): print(n)

def displayeven():
    for n in range(0,101,2): print(n)

te = Thread(target = displayodd)
to = Thread(target = displayeven)


te.start()
to.start()
