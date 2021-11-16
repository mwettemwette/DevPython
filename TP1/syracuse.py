#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:32:56 2021

@author: michel.courbin
"""

def syracuse(n):
    if n == 0 or type(n) != int :
        return "YOUSK2"
    if n % 2 == 0 :
        print(n)
        return syracuse(n // 2)
    print(n)
    return n ,syracuse((n*3)+1)

def altitude_max(n,k):
    if n == 0 or type(n) != int or type(k) != int:
        return "YOUSK2"
    if n == 1 :
        return k
    if n % 2 == 0 :
        return altitude_max(n//2 , k)
    if (3*n)+1 > k :
        k = (3 * n) + 1
    return altitude_max((3*n) + 1 , k)

def temps_de_vol(n,k):
    if n == 0 or type(n) != int or type(k) != int:
        return "YOUSK2"
    if n == 1 :
        return k
    if n % 2 == 0 :
        k+=1
        return temps_de_vol(n//2 , k)
    k+=1
    return temps_de_vol( (3*n) + 1 , k)

def plus_long(n):
    k = 0
    l = 0
    for i in range(1,n):
        if k < temps_de_vol(i,i) :
            k = temps_de_vol(i,i)
            l = i
    return l

def plus_haut(n):
    k=0
    l=0
    for i in range(1,n):
        if k < altitude_max(i, i):
            k = altitude_max(i, i)
            l = i
    return l