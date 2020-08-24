# -*- coding: UTF8 -*-
import re
readFile = open("strings.txt","r")
lines = readFile.readlines()
for i in lines:
    if(bool(re.match('^[a-zA-Z0-9]*$',i))==True):
        print(i[:-1],"was ok.")
    else:
        print(i[:-1],"was invalid.")
