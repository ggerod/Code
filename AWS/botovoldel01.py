#!/usr/local/bin/python3
import boto3

ec2 = boto3.resource('ec2')

Vols = ['vol-0199dfe9b76d8541d','vol-02130a18d990fc2d3','vol-02e820252af886b6e','vol-035e2f9fdbe53dc6e','vol-040361b255d156f93','vol-062418c2d3de35b13','vol-0800d85c7336925a6','vol-082ab0985f05138a2','vol-09d25543142b95b35','vol-0a09323fc9dba7b45','vol-0aabcfc6994818311','vol-0ac910b496391fb79','vol-0b724d2e2f577c042','vol-0bc071591794818c1','vol-0c5f7cf7191c4303f','vol-0e6758ea01e39d2f0','vol-0ef82188696cbf5e8','vol-0f00f1cf168be09f4']

for Vol in Vols:
    print("=================================================================")
    print(Vol)
    gvol = ec2.Volume(Vol)
    print(gvol.attachments)
    print(gvol.describe_status())
    print(gvol.state)
    gvol.delete()


