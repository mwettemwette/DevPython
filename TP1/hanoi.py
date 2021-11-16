#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:30:50 2021

@author: michel.courbin
"""

def Hanoi(n,A,B,C):
    if n==1:
        print("Disque du plot",A,"vers le plot",B)
        return 
    Hanoi(n-1, A, C, B)
    print("Disque du plot",A,"vers le plot",B)
    Hanoi(n-1, C, B, A)

def Hanoi_comptage(n,A,B,C,k):
    if n==1:
        print("Disque du plot",A,"vers le plot",B ,"avec",k, "mouvements")
        return k
    k+=1
    Hanoi_comptage(n-1, A, C, B,k)
    print("Disque du plot",A,"vers le plot",B)
    k+=1
    Hanoi_comptage(n-1, C, B, A,k)