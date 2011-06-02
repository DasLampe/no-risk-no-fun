# -*- coding: utf-8 -*-
import os, re
from config import config

class continents:
    def __init__(self, countries):
        self.continentsList = self.get_continent_list()
        self.countriesList    = countries.countriesList
        
    def get_continent(self, country_id):
        continent_id        = self.get_continent_id(country_id)
        return continent_id[0]
         
    def get_continent_list(self):
        read_config = config()
        return read_config.read_config("maps", "data.map", "continents")
        
    def get_continent_id(self, country_id):
        return self.continentsList[int(self.countriesList[country_id][1])]
        