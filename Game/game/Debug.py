'''
Created on Jan 29, 2014

@author: otrebor
'''

debug = True

def Log(msg):
    if debug:
        print msg

def LogError(msg):
    if debug:
        print "Error: %(s)" % (msg)
