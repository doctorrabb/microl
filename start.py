#!/usr/bin/python

from sys import path
import os

path.insert(0, os.path.realpath (os.path.dirname(__file__)) + '/modules/')

import microl_server

def main ():
    
    microl_server.init ()
    
    cfg_str = ''
    conf = open ('/usr/bin/microl/config.json')

    for i in conf.readlines():
        cfg_str += i
        
    microl_server.serv (cfg_str)
    
if __name__ == '__main__': main ()