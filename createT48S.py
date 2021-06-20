#!/usr/bin/python3

from db import database
import sys
import os

db = database()
lines = db.getAll()
lineDict = {}
for line in lines:
    lineDict[line[1]] = line[2]

folder   = 'T48S'
fileNameSource = '000.GUI.English.lang'
fileNameTarget = '017.GUI.Dutch.lang'

f = open(os.path.join(folder, fileNameTarget), "w")
f.write("[ Lang ]\n\n")

with open(os.path.join(folder, fileNameSource)) as fp:
    for line in fp:
        line = line.strip()
        
        if line == '[ Lang ]' or line == '':
            continue

        en, nl = line.split(' = ')
        en = en[1:-1]
        nl = nl[1:-1]

        if en in lineDict:
            f.write('"%s" = "%s"\n'%(en, lineDict[en]))
        else:
            f.write('"%s" = "%s"\n'%(en, nl))


