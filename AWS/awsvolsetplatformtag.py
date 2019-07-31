#!/usr/local/bin/python3
import subprocess
import json

DRYRUN=0
vollistfile = input("What is the name of the file containing the volume list to update tags: ")
voltag = input("What is the Platform tag name you want to set (e.g. XDP, MeshWifi): ")

file = open(vollistfile, "r")
for line in file:
   VolID = line.rstrip()
   if (DRYRUN == 0):
      print(VolID,"- setting platform to:",voltag)
      #aws ec2 create-tags --resources vol-01ce81e7da5fd0e39 --tags Key=Name,Value=xdpurepw-w2c-01.xdp.comcast.net
      setplatform="Key=Platform,Value="+voltag
      subprocess.run(["aws","ec2","create-tags","--resources", VolID, "--tags", setplatform],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
