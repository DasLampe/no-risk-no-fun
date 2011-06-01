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
			row		= row[:-2].split(seperator)

			if readFile == True and re.search(r"\[.*\]", row[0]) != None:
				readFile	= False	
				break			
			if row[0] == "["+section+"]":
				readFile = True
				continue
			
			if readFile == True and row[0] != "":
				list[int(row[0])]	= (row[1] , row[2] )
		file.close()
		return list