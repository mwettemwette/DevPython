#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:24:47 2021

@author: michel.courbin
"""

def mesImpots(revenu) :
    if revenu < 0 :
        return "Entrez un revenu valide" 
    if revenu <= 10084 :
        return 0
    if revenu <= 25710 :
        return round(((revenu-10084) * 11 /100),2)
    if revenu <= 73516 :
        return round(((( revenu - 25710 ) * 30 / 100) + mesImpots(25710)),2)
    if revenu <= 158122 :
        return round(((( revenu - 73516 ) * 41 / 100 ) + mesImpots(73516)),2)
    if revenu >= 158123 :
        return round(((( revenu - 158122 ) * 45 / 100 ) + mesImpots(158122)),2)
    