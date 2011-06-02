# -*- coding: utf-8 -*-
import os, re
from config import config

class country:
	def __init__(self, gray_map):
		self.gray_map		= gray_map
		self.countriesList	= self.get_country_list()
		
	def get_country(self, click_pos):
		country_id		= self.get_country_id(click_pos)
		
		try:
			return self.countriesList[country_id][0]
		except:
			return 
	
	def get_country_id(self, click_pos):
		color	= self.gray_map.get_at(click_pos)
		
		if color[0] < 255:
			return color[0]
		else:
			return 0
	
	def get_country_list(self):
		read_config	= config()
		return read_config.read_config("maps", "data.map", "countries")
	
	def update_countries(self, armie):
			self.draw_army2country(armie)
			
	def draw_army2country(self, armie, country_id):
		return armie.get_army(country_id)
			
			
		