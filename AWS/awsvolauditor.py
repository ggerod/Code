#!/usr/local/bin/python3
import subprocess
import json

dvolout = subprocess.run(["aws","ec2","describe-volumes"],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
voldata = json.loads(dvolout.stdout)

print("length of voldata volumes = ",len(voldata['Volumes']))
print("VolIndex:VolID:InstanceID:NameTag:PlatformTag")
for k in range(len(voldata['Volumes'])):
   if (len(voldata['Volumes'][k]['Attachments']) == 0):
      continue
   volid = (voldata['Volumes'][k]['Attachments'][0]['VolumeId'])
   instid = (voldata['Volumes'][k]['Attachments'][0]['InstanceId'])

   #aws ec2 describe-tags --filters "Name=resource-id,Values=vol-00ea747db054a183d"
   RID = "Name=resource-id,Values="+volid
   volinfoout = subprocess.run(["aws","ec2","describe-tags","--filters", RID],universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   volinfodata = json.loads(volinfoout.stdout)
   print(str((k + 1))+":",end="")
   print(volid+":"+instid+":",end="")

   #try to get Name and Platform tag info
   for tag in (volinfodata['Tags']):
      if (tag['Key'] == "Name"):
         print(tag['Value'],end="")
   print(":",end="")

   for tag in (volinfodata['Tags']):
      if (tag['Key'] == "Platform"):
         print(tag['Value'],end="")
   print()
