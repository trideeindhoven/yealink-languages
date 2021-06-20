#!/usr/bin/python3

from db import database
import sys

db = database()

with open('T48S/017.GUI.Dutch.lang') as fp:
    for line in fp:
        line = line.strip()
        
        if line == '[ Lang ]' or line == '':
            continue

        en, nl = line.split(' = ')
        en = en[1:-1]
        nl = nl[1:-1]

        if not db.exists(en):
            print("Adding %s -> %s to database"%(en,nl) )
            db.addTranslation(en,nl)

with open('T41S/017.GUI.Dutch.lang') as fp:
    for line in fp:
        line = line.strip()
        
        if line == '[ Lang ]' or line == '':
            continue

        en, nl = line.split(' = ')
        en = en[1:-1]
        nl = nl[1:-1]

        if not db.exists(en):
            print("Adding %s -> %s to database"%(en,nl) )
            db.addTranslation(en,nl)

with open('T46G/014.GUI.Dutch.lang') as fp:
    for line in fp:
        line = line.strip()
        
        if line == '[ Lang ]' or line == '':
            continue

        en, nl = line.split('"="')
        en = en[1:]
        nl = nl[:-1]

        if not db.exists(en):
            print("Adding %s -> %s to database"%(en,nl) )
            db.addTranslation(en,nl)

with open('dutchtrans.lang') as fp:
    for line in fp:
        line = line.strip()
        
        if line == '[ Lang ]' or line == '':
            continue

        en, nl = line.split('"="')
        en = en[1:]
        nl = nl[:-1]

        if not db.exists(en):
            print("Adding %s -> %s to database"%(en,nl) )
            #db.addTranslation(en,nl)
        elif not db.done(en):
            print("Updating %s -> %s"%(en,nl) )


