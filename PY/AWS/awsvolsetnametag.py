#!/usr/local/bin/python3
import subprocess
import json

DRYRUN=0
filename = "/Users/ggerod/WORK/AWS/volaudit01.out"
file = open(filename, "r")
for line in file:
   line = line.rstrip()
   parts = line.split(':')
   VolID = parts[1]
   parts[3] = parts[3].strip()
   print(line,"  - ",end="")
   if (len(parts[3]) > 0):
      print("Do Nothing.  Already set")
      continue
   #Print Name from the Instance information
   INID = "--instance-id="+parts[2]
   instinfoout = subprocess.run(["aws","ec2","describe-instances",INID],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   if (instinfoout.returncode == 0):
      instinfodata = json.loads(instinfoout.stdout)
      if (len(instinfodata['Reservations']) == 0):
         print()
         continue
      for element in (instinfodata['Reservations'][0]['Instances'][0]['Tags']):
         if (element['Key'] == "Name"):
            instancename=element['Value']
            print("Set to: ",instancename)
            if (DRYRUN == 0):
               #set the Name tag of the volume
               #aws ec2 create-tags --resources vol-01ce81e7da5fd0e39 --tags Key=Name,Value=xdpurepw-w2c-01.xdp.comcast.net
               setname="Key=Name,Value="+instancename
               subprocess.run(["aws","ec2","create-tags","--resources", VolID, "--tags", setname],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   else:
      print()
