#!/usr/bin/python2.7
import subprocess
import json
import datetime
import time


hevout = subprocess.Popen(["aws","health","describe-events","--filter","eventStatusCodes=upcoming"],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
evout = hevout.communicate()[0]
#print(evout)

evdata = json.loads(evout)
#print(evdata)

ec=0
for event in evdata['events']:
   print("------------------------------------------------------------")
   #print event
   region = event['region']
   ec+=1
   print "Event ",ec,":"
   print event['eventTypeCode']
   print "region = ",region
   #print event['startTime']
   stime2 = str(datetime.datetime.fromtimestamp(event['startTime']))
   print "start time = ",stime2
   tnow = time.time()
   tdelta =  event['startTime'] - tnow
   #print "tdelta = ",tdelta
   tdiff = str(datetime.timedelta(seconds=tdelta))
   print "which is coming up in: ",tdiff
   earn = event['arn']
   #print("earn = ",earn)
   EA = "eventArns="+earn
   EA2 = "--event-arns "+earn


   #print out affected entity info
   hentout = subprocess.Popen(["aws","health","describe-affected-entities","--filter",EA],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   entout = hentout.communicate()[0]
   entdata = json.loads(entout)
   #print(entdata)
   for entity in entdata['entities']:
      #print(entity)
      eid = entity['entityValue']
      IIP = "--instance-id="+eid
      #print(IIP)
      hentinfoout = subprocess.Popen(["aws","ec2","describe-instances",IIP],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      entinfoout, errcode = hentinfoout.communicate()
      #print("entinfoout = ")
      #print(entinfoout)
      if (errcode == ""):
         entinfodata = json.loads(entinfoout)
         #print("entinfodata = ")
         #print(entinfodata)
         gdata = entinfodata['Reservations']
         gdata = (((entinfodata['Reservations'][0])['Instances'])[0])
         print "IP address = ",gdata['PrivateIpAddress']
         print "project name = ",gdata['KeyName']
         if ('Tags' in gdata):
            #print(gdata['Tags'])
            print gdata['Tags'][3]['Key']," = ",gdata['Tags'][3]['Value']
            print gdata['Tags'][4]['Key']," = ",gdata['Tags'][4]['Value']
            print gdata['Tags'][5]['Key']," = ",gdata['Tags'][5]['Value']
         print
   print


   # Print more event description info
   hevdout = subprocess.Popen(["aws","health","describe-event-details","--event-arns",earn],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   evdout, errcode = hevdout.communicate()
   #print(evdout)
   if (errcode == ""):
      print "Details:"
      evddata = json.loads(evdout)
      print evddata['successfulSet'][0]['eventDescription']['latestDescription']

print("------------------------------------------------------------")
