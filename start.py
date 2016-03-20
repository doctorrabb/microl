#!/usr/bin/python

from sys import path
import os
from threading import Thread
import time
import json

path.insert(0, os.path.realpath (os.path.dirname(__file__)) + '/modules/')

import microl_server
import command_block


def main ():
    
    microl_server.init ()
    
    cfg_str = ''
    conf = open ('/etc/microl/config.json')
    
    
    for i in conf.readlines():
        cfg_str += i
    
    jscf = json.loads (cfg_str)
    
    if jscf ['pythonScriptsExec']:
        for i in os.listdir(os.path.realpath (os.path.dirname (__file__)) + '/py_scripts/'):
            Thread (target=os.system, args=('python ' + os.path.realpath(os.path.dirname(__file__)) + '/py_scripts/' + i,)).start ()
    
    if jscf ['rubyScriptsExec']:
        for i in os.listdir(os.path.realpath (os.path.dirname (__file__)) + '/rb_scripts/'):
            Thread (target=os.system, args=('ruby ' + os.path.realpath(os.path.dirname(__file__)) + '/rb_scripts/' + i,)).start () 
    
    microl_server.serv (cfg_str)
    
if __name__ == '__main__': main ()
