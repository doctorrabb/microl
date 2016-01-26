from sys import path
import os

import pyperclip

path.insert (0, os.path.realpath(os.path.dirname (__file__)))

def run ():
    while True:
        command = raw_input('>>> ').split (' ')
        if command[0] == 'ban':
            blacklist_file = open ('/usr/bin/microl/blacklist.lst', 'a')
            blacklist_file.write (command [1])
            blacklist_file.close ()
        elif command [0] == 'exit':
            pyperclip.copy ('exit')
            break
        else:
            print 'Command not found!'