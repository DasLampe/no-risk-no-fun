# -*- coding: utf-8 -*-
import sys, os

import pygame
from pygame import Rect, Color
from pygame.sprite import Sprite

def run_game():
    # Game parameters
    SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
    BG_COLOR = 150, 150, 80

    pygame.init()
    screen = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    
    tux			= pygame.image.load(os.path.join('data', 'tux.png')).convert_alpha()   
    clickPos	= (-1,-1)
    
    while True:
        clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
            	clickPos = event.pos
        
        # Redraw the background
        screen.fill(BG_COLOR)
        
        screen.blit(tux, (0,0))
        
        if tux.get_rect().collidepoint(clickPos[0], clickPos[1]) == True:
        	print "CLICK!"
        	sys.exit()
        	
		
        pygame.display.flip()



run_game()