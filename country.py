# -*- coding: utf-8 -*-
import os, re, pygame
from config import config

class country:
	def __init__(self, gray_map, screen):
		self.gray_map		= gray_map
		self.screen			= screen
		self.countriesList	= self.get_country_list()
		self.neighborList	= self.get_neighbor_list()
		
	def get_country(self, click_pos):
		country_id		= self.get_country_id(click_pos)
		
		try:
			return self.countriesList[country_id][0]
		except:
			return False
	
	def get_country_id(self, click_pos):
		color	= self.gray_map.get_at(click_pos)
		
		if color[0] < 255:
			return color[0]
		else:
			return 0
	
	def get_country_list(self):
		read_config	= config()
		return read_config.read_config("maps", "data.map", "countries")
	
	def get_neighbor_list(self):
		read_config	= config()
		return read_config.read_config("maps", "data.map", "neighbor")
	
	def update_countries(self, armie):
			self.draw_army2country(armie)
			
	def draw_army2country(self, armie):
		for country_id in self.countriesList.keys():
			font 		= pygame.font.Font(os.path.join("data", "font", "arial.ttf"), 14)
			text 		= font.render(str(armie.get_army(country_id)), True, (255,255, 255))
			circlePos	= (int(self.countriesList[country_id][2]), int(self.countriesList[country_id][3]))
			
			circle		= pygame.draw.circle(self.screen, (0,0,0), circlePos, 11)
			textPos		= (circle[0]+3, circle[1]+3)
			self.screen.blit(text, textPos)
	
	def is_country(self, country_id):
		if country_id > 0:
			return True
		return False
	
	def is_neighbor(self, country1_id, country2_id):
		for i in xrange(0, len(self.neighborList[country1_id])-1):
			if int(self.neighborList[country1_id][i]) == int(country2_id):
				return True
		return False
			
		