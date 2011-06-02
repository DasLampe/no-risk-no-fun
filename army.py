# -*- coding: utf-8 -*-

class army:
	def __init__(self, countries):
		self.army2country	= countries.get_country_list()
	
	def set_army(self, country_id, number):
		if len(self.army2country[country_id]) == 4:
			self.army2country[country_id].append(number)
		else:
			self.army2country[country_id][4]	+= int(number)
			
	def get_army(self, country_id):
		if len(self.army2country[country_id]) == 4:
			return 0
		else:
			return self.army2country[country_id][4]