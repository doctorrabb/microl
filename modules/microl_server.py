import socket
import json  
import os
from sys import path
import pyperclip
from threading import Thread

path.insert(0, os.path.realpath (os.path.dirname (__file__)) + '/modules/')

from output import *
import command_block

DEFAULT_CONFIG = '''
{
   "host" : "localhost",
   "port" : 80,
   "max_clients" : 1,
   "defaultWebServerPath" : "/home/''' + os.getlogin () + '''/microl"
}
''' 

DEFAULT_HTML_PAGE = '''
<head>
  <title>Microl Web Server</title>
</head>
<body>
  <center>Microl Web Server v0.01</center>
</body>
'''

BAN_IP_HTML_PAGE = '''
<head><title>Access Error!</title></head>
<body>
<center><h1><font color="red">Your IP in the blacklist!</font></h1></center>
</body>
'''
    
def init ():
    if not os.path.isdir('/usr/bin/microl'):
        os.mkdir ('/usr/bin/microl')
        os.mkdir ('/home/' + os.getlogin () + '/microl')
        f1 = open ('/home/' + os.getlogin () + '/microl/index.html', 'w')
        f1.write (DEFAULT_HTML_PAGE)
        f1.close ()
        
        f2 = open ('/usr/bin/microl/config.json', 'w')
        f2.write (DEFAULT_CONFIG)
        f2.close ()  
        
        f3 = open ('/usr/bin/microl/blacklist.lst', 'w')
        f3.write ('')
        f3.close ()
    
def serv (json_config):
    
    json_config = json.loads (json_config)
    
    HOST = json_config ['host']
    PORT = json_config ['port']

    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind ((HOST, PORT))
    s.listen (json_config ['max_clients'])
    
    
    print INFO + 'Server started\nHost: ' + HOST + '\nPort: ' + str (PORT)
    
    code = ''
    
    f = None
    
    if not json_config ['defaultWebServerPath'].endswith ('/'): 
        f = open ( json_config ['defaultWebServerPath'] + '/index.html', 'r')
    else:
        f = open ( json_config ['defaultWebServerPath'] + 'index.html', 'r')

    for i in f.readlines(): code += i

    while True:
        
            con, addr = s.accept()
        
            banned = False
        
            for i in open ('/usr/bin/microl/blacklist.lst', 'r').readlines ():
            
                if addr [0] == i.strip ('\n'):
                
                    banned = True
                
                    con.sendall (BAN_IP_HTML_PAGE)
                    con.close ()
        
            if not banned:
               con.sendall (code)
               con.close ()
