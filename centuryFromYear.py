#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:47:27 2022

@author: faikmermer
"""

def solution(year):
    yy = int(year / 100)
    
    while (year >= 1):
        if (year % 100 == 0):
            return yy
        else:
            return yy + 1

solution(1905)

