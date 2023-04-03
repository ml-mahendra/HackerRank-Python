# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:42:17 2023

@author: Mahendra Nath reddy E
"""


# Method -1

"""
def print_full_name(first, last):
    
    common_tag = "You just delved into python."
    print("Hello", first, last+"!",common_tag)

"""

# Method - 2
def print_full_name(first,last):
    print(f"Hello {first} {last}!","You just delved into python")
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)