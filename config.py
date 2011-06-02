# -*- coding: utf-8 -*-
import os, re

class config:
	def __init__(self):
		pass
	
	def read_config(self, dir, file, section, seperator=" "):
		readFile	= False
		list		= {}
		
		file		= open(os.path.join(dir, file), "r")
		for row in file:
			row		= row.strip()
			row		= row.split(seperator)

			if readFile == True and re.search(r"\[.*\]", row[0]) != None:
				readFile	= False
				break			
			if row[0] == "["+section+"]":
				readFile = True
				continue
			
			if readFile == True and row[0] != "":
				list[int(row[0])]	= []
				for data in xrange(0, len(row)-1):
					list[int(row[0])].append(row[data+1])
		file.close()
		return list
	
	def append_config(self, dir, file, section, data, seperator=" "):
		pass