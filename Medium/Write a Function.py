# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 13:47:32 2023

@author: Mahendra nath reddy E
"""

def is_leap(year):    
    if(year%4==0 and year%100 !=0 or year%400==0): 
        return True
    else:
        return False

year = int(input())