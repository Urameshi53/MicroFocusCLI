# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:57:36 2024

@author: Daniel Akey
"""



class School(object):
    def __init__(self, name, location):
        self.name = name 
        self.location = location
        self.key = None
        
    def buyKey(self, m):
        self.key = m.grantkey(self)
        
    def print_key(self):
        print(self.key, self.key.proc_date_formatted, self.key.exp_date_formatted)
    
    def __str__(self):
        return self.name
        