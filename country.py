# -*- coding: utf-8 -*-
import os, re

from config import config as config
from army import army


class country:
	def __init__(self):
		self.countriesList	= self.get_country_list()
		pass
		
	def get_country(self, gray_map, click_pos):
		country_id		= self.get_country_id(gray_map, click_pos)
		  
		return self.countriesList[country_id][0]
	
	def get_country_id(self, gray_map, click_pos):
		color	= gray_map.get_at(click_pos)
		
		if color[0] < 255:
			return color[0]
		else:
			return 0
	
	def get_country_list(self):
		read_config	= config()
		return read_config.read_config("maps", "data.map", "countries")
	
	def update_countries(self):
			self.draw_army2country()
			
	def draw_army2country(self):
		pass
			
			
		