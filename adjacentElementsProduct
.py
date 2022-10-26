#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:08:52 2022

@author: faikmermer
"""

def solution(inputArray):
    Enbuyuk = inputArray[0] * inputArray [1]
    
    for i in range(len(inputArray) -1):
    
        buyuk = inputArray[i] * inputArray[i + 1]
        if (buyuk > Enbuyuk):
            Enbuyuk = buyuk
    
    return Enbuyuk

solution([-1, -2])