# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:10:09 2024

@author: Daniel Akey
"""


import datetime
from accesskey import AccessKey
from school import School

'''
Access Key Manager - Features
    1. Key Generation
    2. Key Storage
    3. Key distribution
    4. Key Rotation
    5. Key Revocation
    6. Access Control
    7. Audit & Loggin

'''

class Mother(object):
    def __init__(self):
        self.keys = []
        self.data = {}
    
    def generate_key(self, school):
        a = AccessKey()
        self.keys.append(a)
        self.data[school] = a
        return a 
    
    def grantkey(self, school):
        if not school.key:
            key = self.generate_key(school)
            return key
        elif school.key.status == 'Expired':
            key = self.generate_key(school)
            return key
        elif school.key.status == 'Revoked':
            print(str(school), 'Your access key has been revoked')
        else:
            print(str(school),'You already have an active key')
    
    def revoke_key(self, key):
        pass
    
    def rotate_key(self, key):
        pass
    
    def print_keys(self):
        for i in self.keys:
            print(i, i.status, i.proc_date_formatted)
            
    def print_data(self):
        for i in self.data.keys():
            print(str(i), str(self.data[i]), self.data[i].status)
    

    
    
    
    
    
    
    
    