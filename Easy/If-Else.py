# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 13:41:54 2023

@author: Mahendra Nath Reddy E
"""

integer = int(input())

if((integer %2 == 0) and (integer in range(2,6))):
    print("Not Weird")
elif((integer%2==0) and (integer in range(6,21))):
    print("Weird")
elif((integer%2==0) and (integer >20)):
    print("Not Weird")
else:
    print("Weird")
    
