#!/usr/local/bin/python3

import os
from splunk_helpers import perform_splunk_query

filename = "wanmaclist"+str(int(list(os.times())[4]))+".txt"
outfile = open(filename, "w")

#print('username =', os.environ.get('SPLUNK_USERNAME', None))
#print('pw =', os.environ.get('SPLUNK_PASSWORD', None))

#query = 'earliest=-1d index=rdk-json sourcetype=rdk-json "searchResult{}.SYS_ERROR_CUJO_cloud_assoc_fail"=* "searchResult{}.cujourlerr_split"=" -1)" searchResult{}.erouterIpv4 != 0.0.0.0 | fields mac, searchResult{}.erouterIpv4 | stats count by mac, searchResult{}.erouterIpv4 | sort -count | where count >95'

query = 'earliest=09/24/2019:06:00:00 latest=09/25/2019:06:00:00 index=rdk-json sourcetype=rdk-json "searchResult{}.SYS_ERROR_CUJO_cloud_assoc_fail"=* "searchResult{}.cujourlerr_split"=" -1)" searchResult{}.erouterIpv4 != 0.0.0.0 | fields mac, searchResult{}.erouterIpv4 | stats count by mac, searchResult{}.erouterIpv4 | sort -count | where count >95'

response = perform_splunk_query(query)
wanmaclist = []
for result in response:
    wanmaclist.append(result['mac'])

#print("\nwanmaclist = ",end="")
#print(wanmaclist)
print("\nlen(wanmaclist) = ",len(wanmaclist))

cmmaclist = []
for wanmac in wanmaclist:
        wanmac = wanmac.replace(":","")
        cmmac = (hex(int(wanmac, base=16) - 2))[2:]
        if (len(cmmac) != 12):
           cmmac = ('0'*(12 - len(cmmac))) + cmmac
        cmmaclist.append(cmmac)
        outfile.write(cmmac+"\n")

outfile.close()
#print("\ncmmaclist = ",end="")
#print(cmmaclist)
print("\nlen(cmmaclist) = ",len(cmmaclist))
