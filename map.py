# -*- coding: utf-8 -*-
import os
import pygame

class map:
	def __init__(self):
		pass
		
	def get_map_color(self, pos):
		image	= self.get_gray_map()
		return image.get_at(pos)
	
	def get_colored_map(self):
		return pygame.image.load(os.path.join("maps", "map_pic.jpg"))
	
	def get_gray_map(self):
		return pygame.image.load(os.path.join("maps", "map.gif"))
	
	def get_mapsize(self):
		image	= self.get_gray_map()
		return image.get_size()
		