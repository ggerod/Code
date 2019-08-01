#!/usr/bin/python2

import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
ENC="f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
IV="f20bdba6ff29eed7b046d1df9fb70000"
BL0="58b1ffb4210a580f748b4ac714c001bd"
BL1="4a61044426fb515dad3f21f18aa577c0"
BL2="bdf302936266926ff37dbf7035d5eeb4"
# Length = 64 bytes/128 hex digits
# AES block size = 128 bits/16 bytes
# Therefore there are 4 blocks, the first of which is the random IV
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                print "We got: %d" % e.code       # Print response code
                print("this was good padding")
                print "guess=",guess," - byte15=",byte15," - byte15mod=",format(byte15mod,'02x')," - BL0=",BL0
                print checkctext
                return True # good padding
            return False # bad padding


# Do M1 (so mod BL0)
byte16=BL0[-2] + BL0[-1]
byte15=BL0[-4] + BL0[-3]
for guess in range(0,256,1):
    po = PaddingOracle()

    byte16mod = int(byte16, 16) ^ 115 ^ 2
    byte15mod = int(byte15, 16) ^ guess ^ 2
    BL0 = BL0[:-4] + format(byte15mod,'02x') + format(byte16mod,'02x')
    checkctext = IV + BL0 + BL1
    
    po.query(checkctext)       # Issue HTTP query with the given argument
