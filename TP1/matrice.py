#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:51:45 2021

@author: michel.courbin
"""
import numpy as np

def multiplication(A,B):
    n = np.shape(A)
    m = np.shape(B)
    if n[1] != m[0] :
        return "YOUSK2"
    C = np.zeros([n[0],m[1]])
    for i in range(n[0]) :
        for j in range(m[1]) :
            for k in range(n[1]) :
                C[i][j] = A[i][k] * B[k][j]
    return C
    