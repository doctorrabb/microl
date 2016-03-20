from sys import path
import os
import json

path.append (os.path.realpath (os.path.dirname (__file__)))

import microl_server

class Parser:

	SCRIPT_BUFFER = {}

	def __init__ (self, script_path):
		self.script = script_path
		
	def parse_and_run (self):
		json_get = json.loads (microl_server.DEFAULT_CONFIG)
		with open (self.script, 'r') as f:
			for i in f.readlines:
				if i == 'BLACKLIST.CLEAR':
					bl_file = open ('/etc/microl/blacklist.lst', 'w')
					bl_file.write ('')
					bl_file.close ()
				elif i.split (' ')[0] == 'BLACKLIST.APPEND':
					bl_file = open ('/etc/microl/blacklist.lst', 'a')
					bl_file.write (i.split (' ')[1])
					bl_file.close ()
				elif i == 'BLACKLIST.GET':
					bl_file = open ('/etc/microl/blacklist.lst', 'r')
					for i in range (len (bl_file.readlines ())): SCRIPT_BUFFER ['blacklist_element_ip' + str (i)] = bl_file.readlines ()[i]
					bl_file.close ()
				elif i.split (' ')[0] == 'OUTPUT.SHOW':
					if i.split (' ')[1] in SCRIPT_BUFFER:
						print SCRIPT_BUFFER [i.split (' ')[1]]
					else:
						print i.split (' ')[1]