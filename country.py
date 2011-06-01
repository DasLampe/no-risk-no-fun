# -*- coding: utf-8 -*-
import os, re

class country:
	def __init__(self):
		pass
		
	def get_country(self, gray_map, click_pos):
		country_id		= self.get_country_id(gray_map, click_pos)
		country_name	= self.get_country_list()
		  
		return country_name[country_id]['name']
	
	def get_country_id(self, gray_map, click_pos):
		color	= gray_map.get_at(click_pos)
		
		if color[0] < 255:
			return color[0]
		else:
			return 0
	
	def get_country_list(self):
		readFile	= False
		list		= {}
		
		file		= open(os.path.join("maps", "data.map"), "r")
		for row in file:
			row		= row[:-2].split(" ")

			if readFile == True and re.search(r"\[.*\]", row[0]) != None:
				readFile	= False	
				break			
			if row[0] == "[countries]":
				readFile = True
				continue
			
			if readFile == True and row[0] != "":
				list[int(row[0])]	= {'name' : row[1] , 'continent' : row[2] }
		file.close()
		return list
			
		