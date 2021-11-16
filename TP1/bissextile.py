#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:11:15 2021

@author: michel.courbin
"""

# Header


def bissextile(annee) :
    if annee % 4 == 0 :
        if annee % 400 == 0 :
            return True
        elif str(annee)[-1] + str(annee)[-2] == '00' :
            return False
        return False

def jours_mois(mois, annee) :
    if not 1 <= mois <=12 or type(mois) != int or type(annee) != int:
        return "YOUSK2"
    if mois == 2 :
        if bissextile(annee) == True :
            return 29
        return 28
    liste_mois = [4,6,9,11]
    if mois in liste_mois :
        return 30
    return 31

def date_valide(jour,mois,annee) :
    if type(jour) == int and type(mois) == int and type(annee) == int :
        if not 1 <= mois <= 12 :
            return False
        elif not 1 <= jour <= jours_mois(mois, annee):
            return False 
        return True
    return False

def verif_date() :
    jour = int(input('DONNE LE JOUR'))
    mois = int(input('DONNE LE MOIS'))
    annee = int(input('DONNE L ANNEE'))
    if date_valide(jour, mois, annee) == True :
        return "Date valide"
    return "Date non valide"
