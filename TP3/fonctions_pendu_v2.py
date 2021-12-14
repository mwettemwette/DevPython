#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme contient toutes les fonctions nécessaires au fonctionnement du jeu du pendu.
        pendu est le corps du programme, il regroupe la boucle du jeu et compte le nombre d'essais restants et le meilleur score
        choix_mot initialise le mot à deviner en le cherchant dans un fichier texte
        initialisation initialise le mot affiché, première lettre et autres occurences dans le mot et met un underscore sinon
        choix_lettre verifie prend une lettre en entrée et vérifie si elle est dans le mot à deviner et vérifie que la lettre, bonne ou mauvaise, n'a pas déjà été entrée
        tes_mauvais vérifie qu'il reste des essais au joueur et diminue ce nombre si sa proposition est mauvaise
        remplacement_lettre remplace dans le mot affiché la lettre correcte au même emplacement que dans le mot à deviner
        verif_fini vérifie que le mot affiché n'a plus de lettres à trouver, s'il reste des lettres à trouver on continue dans pendu dinon on va dans fin
        perdu se déclenche lorsque le joueur n'a plus d'essais disponibles et va dans fin
        fin affiche le meilleur score et le modifie si le score actuel est meilleur et demande au joueur s'il veut rejouer si oui on retourne dans pendu sinon le programme s'arrête 
        
Fait par Michel COURBIN

Created on Tue Dec  7 11:21:45 2021

Tout doux :
"""
from random import randint 


def pendu():
    global essais
    essais = 8
    mot = choix_mot()
    mot_visible = initialisation(mot)
    global lettres_mauvaises
    global meilleur_score
    meilleur_score = 0
    lettres_mauvaises = []
    print(mot_visible)
    verif = 'yousk2'
    while verif == 'yousk2':
        (mot, mot_visible, essais) = choix_lettre(mot, mot_visible, essais)
        print(mot_visible)
        verif = verif_fini(mot_visible)
        if essais == 0 :
            perdu()
            verif = 'fin'
    return ' '

def choix_mot():
    with open("liste_francaise.txt", "r") as file :
        liste = file.readlines()
        longueur_liste = len(liste)
    
    nummot = randint(0, longueur_liste-1)
    mot = liste[nummot].strip()
    if len(mot) < 5 :
        return choix_mot()
    return mot

def choix_lettre(mot, mot_visible, essais):
    lettre = input('Proposition de lettre : ').lower()
    if lettre in mot_visible or lettre in lettres_mauvaises :
        print('La lettre a déjà été entrée')
        return(mot, mot_visible, essais)
    if lettre in mot:
        return (mot, remplacement_lettre(lettre, mot, mot_visible), essais)
    lettres_mauvaises.append(lettre)
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
    global meilleur_score
    global essais
    if essais > meilleur_score:
        meilleur_score = essais
    print('Meilleur score = ' ,meilleur_score)
    reponse = input('Voulez-vous continuer à jouer ? Oui      Non    ').lower()
    reponse_valable = ['oui', 'o', 'yes', 'y', 'no','non','n']
    if reponse not in reponse_valable :
        return fin()
    if reponse == 'no' or reponse =='n' or reponse == 'non' :
        print( "Merci d'avoir joué")
    else :
        return pendu()
        