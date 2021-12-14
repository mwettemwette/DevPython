#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme contient toutes les fonctions nécessaires au fonctionnement du jeu du pendu.

Fait par Michel COURBIN

Created on Tue Dec  7 08:18:45 2021

Tout doux :
- erreur pas une lettre
"""
from random import randint 


def pendu():
    essais = 8
    mot = choix_mot()
    mot_visible = initialisation(mot)
    print(mot_visible)
    verif = 'yousk2'
    while verif == 'yousk2':
        (mot, mot_visible, essais) = choix_lettre(mot, mot_visible, essais)
        print(mot_visible)
        verif = verif_fini(mot_visible)
        print(verif)
        if essais == 0 :
            perdu()
            verif = 'fin'

def choix_mot():
    with open("liste_francaise.txt", "r") as file :
        liste = file.readlines()
        longueur_liste = len(liste)
    
    nummot = randint(0, longueur_liste-1)
    mot = liste[nummot].strip()
   # if len(mot) < 5 :
       print(reponse)
    return mot

def choix_lettre(mot, mot_visible, essais):
    lettre = input('Proposition de lettre : ').lower()
    if lettre in mot:
        return (mot, remplacement_lettre(lettre, mot, mot_visible), essais)
    return (mot, mot_visible, tes_mauvais(essais))
    
def tes_mauvais(essais):
    if essais == 0 :
        perdu()
        return 8
    return essais-1
    

def remplacement_lettre(lettre, mot, mot_visible):
    for i in range(len(mot)):
        if mot[i] == lettre :
            caracteres = list(mot_visible)
            caracteres[i] = lettre
            mot_visible = ''.join(caracteres)
    return mot_visible

def initialisation(mot):
    mot_visible = ''
    for i in range(len(mot)):   
        mot_visible+='_'
    return remplacement_lettre(mot[0], mot, mot_visible)

def verif_fini(mot_visible):
    if not '_' in mot_visible:
        print('Bravo vous avez réussi à trouver le mot')
        return fin()
    return 'yousk2'

def perdu():
    print('Tu es vraiment pas très bon, tu veux recommencer ? ')
    return fin()

def fin():
    reponse = input('Voulez-vous continuer à jouer ? Oui      Non    ').lower()
    reponse_valable = ['oui', 'o', 'yes', 'y', 'no','non','n']
    if reponse not in reponse_valable :
        return fin()
    if reponse == 'no' or reponse =='n' or reponse == 'non' :
        print( "Merci d'avoir joué")
        return ' '
    else :
        return pendu()
        