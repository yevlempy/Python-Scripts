#!/usr/bin/env python
'''
Created on Jan 13, 2012

@author: yevlempy
'''
#Importing proper libraries!
import sys
import re
import time 
import os
import shutil
import string
import json
from tempfile import mkstemp
from shutil import move
from os import remove, close
from xml.dom.minidom import parseString
import fileinput
#Handling Deprecation Warning!
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    import md5,sha
m = [":list", "=>", "Harsh", "Raja", "Baja :P"]
#Converting ctjava.ddl to ctjava_backup.ddl!
shutil.copy2("ctjava.ddl", "ctjava_backup.ddl")
#Taking md5sum of ctjava_backup.ddl and comparing it with the old ctjava.ddl!
a = md5.new(file("ctjava_backup.ddl").read()).hexdigest()
b = md5.new(file("ctjava.ddl").read()).hexdigest()
print a
print b
if a == b:
    print "The md5sum of both ddl file matches"
else:
    print "Sorry md5sum of both ddl file does not matches"
#Opening startup.xml and parsing it i.e Extracting whatsoever elements are there inside applicationname tag and dumping them for proper format as a json!
file = open('startup.xml','r')
data = file.read()
file.close()
dom = parseString(data)
xmlTag = dom.getElementsByTagName('applicationname')
ddllist = []
for x in range(0, xmlTag.length):
    for y in range(x+1, xmlTag.length):
        if (xmlTag[x].childNodes[0].nodeValue == xmlTag[y].childNodes[0].nodeValue):
            ddllist.append (xmlTag[x].childNodes[0].nodeValue)
k = json.dumps(ddllist)
print k
#TODO To replace the duplicated items and append "All" at the starting of the list!
o = open("ctjavanew.ddl","w")
for line in open('ctjava.ddl').readlines():
    if (re.match('[\s]+:list =>',line)):
        o.write( re.sub('\[(.*)',k,line))
    else:
        o.write(line)
o.close()
os.rename("ctjavanew.ddl","ctjava.ddl")
