#!/usr/local/bin/python3
from threading import *
from time import sleep

def dfunc(host):
   print("host = ",host)
   print("starting thread: ", current_thread() )
   sleep(2)
   print("ending thread: ", current_thread())


t1 = Thread(target=dfunc)
t2 = Thread(target=dfunc)
print("starting funcs")
t1.start(host="glen")
#t2.start()

"""
t=[0,0,0]
for i in range(3):
   print(i)
   t[i] = (Thread(target=dfunc("abc")))

print(t)
"""
