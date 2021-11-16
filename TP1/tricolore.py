#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:00:38 2021

@author: michel.courbin
"""

def tricolore(n):
    carre = n**2
    s_carre = str(carre)
    if '0' in s_carre or '2' in s_carre or '3' in s_carre or '5' in s_carre or '6' in s_carre or '7' in s_carre or '8' in s_carre:
        return False
    return True

def tous_les_tricolores(n):
    liste_tricolores = []
    for i in range(1,n):
        if tricolore(i):
            liste_tricolores.append(i)
    return liste_tricolores
