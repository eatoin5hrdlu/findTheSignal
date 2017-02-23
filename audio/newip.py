#!/usr/bin/python
from __future__ import print_function
import os, sys, time, subprocess

ipFile = 'lastIP'
fIP = open(ipFile,'r')
oldip = fIP.read()[:-1]
fIP.close()

time.sleep(1)
getip = ['hostname','-I']
proc = subprocess.Popen(getip, stdout=subprocess.PIPE)
newip = "   ".join(proc.stdout.read().strip().split())

if (newip == oldip) :
    sys.exit(0)
else :
    fIP = open(ipFile,'w')
    print(newip,file=fIP)
    fIP.close()
    sys.exit(1)

