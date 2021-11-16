#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:43:08 2021

@author: michel.courbin
"""

def amicaux(n,m):
    som_div_n = 0
    som_div_m = 0
    for i in range(1,n+1):
        if n % i == 0 :
            som_div_n+=i
    for j in range(1,m+1):
        if m % j == 0 :
            som_div_m+=j
    if som_div_m != som_div_n or som_div_n != n+m:
        return "Pas amicaux lel"
    return "Ce sont des nombres amicaux"
        


        