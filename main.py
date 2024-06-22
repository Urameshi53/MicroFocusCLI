# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:26:21 2024

@author: Daniel Akey
"""

from mother import Mother 
from school import School
from accesskey import AccessKey 

s1 = School('KNUST', 'Kumasi')
s2 = School('UDS', 'Accra')
s3 = School('UCC', 'Cape Coast')
s4 = School('UG', 'Accra')
s5 = School('KSTU','Kumasi')

m = Mother()
s1.buyKey(m)
s1.buyKey(m)
s2.buyKey(m)
s3.buyKey(m)
s4.buyKey(m)

# m.print_keys()
m.print_data()
# s1.print_key()