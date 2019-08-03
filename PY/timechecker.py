#!/usr/bin/python3
#actuals>>
#   1 billion >>   71 s
# 100 billion >> 8584 s
#
#project >>
#   1 trillion > 85840s = 23.84 hrs  >>> 1 day per trillion or about 2.74 years per quadrillion (this was way off)
#
#
#   There are 66,761 blocks of 100 billion hops of distance 6
#  3790:59 primefactor6f.p - yielded 400 billion hops of distance 6 with two checks per hop
#  4953:09 primefactor6f.p - yielded 500 billion hops of distance 6 with two checks per hop
#  5642:41 primefactor6f.p - yielded 600 billion hops of distance 6 with two checks per hop (this was within 10 minutes of update)
#  6656:03 primefactor6f.p - yielded 700 billion hops of distance 6 with two checks per hop (this was within 90 minutes of update)
#  7697:51 primefactor6f.p - yielded 800 billion hops of distance 6 with two checks per hop (this was within 180 minutes of update)
#  8507:22 primefactor6f.p - yielded 900 billion hops of distance 6 with two checks per hop (this was within 1 minute of update)
#  980:16  primefactor6f.p - yielded 100 billion hops of distance 6 with two checks per hop (this was within 7 minutes of update)
#  2075:33 primefactor6f.p - yielded 200 billion hops of distance 6 with two checks per hop (this was within 137 minutes of update)
#  13361:28 primefactor6f.p - yielded 1400 billion hops of distance 6 with two checks per hop (this was within 157 minutes of update)
#  14300:22 primefactor6f.p - yielded 1500 billion hops of distance 6 with two checks per hop (this was within 136 minutes of update)
#  15141:38 primefactor6f.p - yielded 1600 billion hops of distance 6 with two checks per hop (this was within 3 minutes of update)
#  16172:24 primefactor6f.p - yielded 1700 billion hops of distance 6 with two checks per hop (this was within 23 minutes of update)
#  18187:47 primefactor6f.p - yielded 1900 billion hops of distance 6 with two checks per hop (this was within 6 minutes of update)
#  19223:53 primefactor6f.p - yielded 2000 billion hops of distance 6 with two checks per hop (this was within 70 minutes of update)
#

count=100000000000
for i in range(count):
    j=i/2
print("time for ",count,"iterations with a single operation is:")
