#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:49:02 2022

@author: faikmermer
"""

def solution(inputString):
    low = inputString.lower().replace(" ", "")
    
    reverse = low[::-1]
    
    if (reverse == low):
        return True
    else:
        return False
        
solution("aabaa")

