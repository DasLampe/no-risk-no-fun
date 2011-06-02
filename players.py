# -*- coding: utf-8 -*-
class players:
	def __init__(self):
		self.player_army		= 22 #Number of Army to set
		self.player_countries	= [] #List of country ids
		
	def get_player_army(self):
		return self.player_army
	
	def set_player_army(self, number):
		self.player_army		+= number
		
	def set_player_countries(self, country_id, action="add"):
		if action == "add":
			self.player_countries	+= country_id
		else:
			for i in xrange(0, len(self.player_countries)-1):
				if country_id == self.player_countries[i]:
					self.player_countries.remove(i)
					
	def get_player_countries(self):
		return self.player_countries