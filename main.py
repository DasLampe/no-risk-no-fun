# -*- coding: utf-8 -*-
import sys, os

import pygame

from country import country
from continents import continents
from map import map
from army import army

def run_game():
	pygame.init()
	
	maps				= map()
	gray_map			= maps.get_gray_map()
	colored_map			= maps.get_colored_map()
	
	screen_size			= maps.get_mapsize()
	
	SCREEN_WIDTH		= screen_size[0]
	SCREEN_HEIGHT 		= screen_size[1]
	BG_COLOR 			= 150, 150, 80

	screen 				= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	
	countries			= country(gray_map, screen)
	armie				= army(countries)
	continent			= continents(countries)

	
	clock 				= pygame.time.Clock()
	
	armie.set_army(12, 88)
	
	screen.fill(BG_COLOR)
	screen.blit(colored_map, (0,0))
    
	while True:
		clock.tick(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if countries.is_country(countries.get_country_id(event.pos)) == True:
					print countries.get_country(event.pos),
					print continent.get_continent(countries.get_country_id(event.pos))

		countries.update_countries(armie)
		pygame.display.flip()

run_game()
