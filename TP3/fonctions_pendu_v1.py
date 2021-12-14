#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme contient toutes les fonctions nécessaires au fonctionnement du jeu du pendu.
        pendu est le corps du programme, il regroupe la boucle du jeu et compte le nombre d'essais restants
        choix_mot initialise le mot à deviner en le cherchant dans un fichier texte
        initialisation initialise le mot affiché, première lettre et autres occurences dans le mot et met un underscore sinon
        choix_lettre verifie prend une lettre en entrée et vérifie si elle est dans le mot à deviner
        tes_mauvais vérifie qu'il reste des essais au joueur et diminue ce nombre si sa proposition est mauvaise
        remplacement_lettre remplace dans le mot affiché la lettre correcte au même emplacement que dans le mot à deviner
        verif_fini vérifie que le mot affiché n'a plus de lettres à trouver, s'il reste des lettres à trouver on continue dans pendu dinon on va dans fin
        perdu se déclenche lorsque le joueur n'a plus d'essais disponibles et va dans fin
        fin demande au joueur s'il veut rejouer si oui on retourne dans pendu sinon le programme s'arrête
        
Fait par Michel COURBIN

Created on Tue Dec  7 08:18:45 2021

Tout doux :

"""
from random import randint 


def pendu():
    #initialisation de la partie
    essais = 8
    
    #on choisit le mot
    mot = choix_mot()
    
    #on initialise le mot à afficher
    mot_visible = initialisation(mot) 
    print(mot_visible)
    
    verif = 'yousk2' #condition pour continuer à chercher des lettres
    
    while verif == 'yousk2':
        # on veut une proposition de lettres donc on passe dans choix_lettre
        (mot, mot_visible, essais) = choix_lettre(mot, mot_visible, essais)
        print(mot_visible)
        #on vérifie qu'il reste des lettres à trouver
        verif = verif_fini(mot_visible)
        if essais == 0 :
            #on arrête si on a perdu
            perdu()
            verif = 'fin'
    return ' '



def choix_mot():
    #on prend une liste de mots 
    
    with open("liste_francaise.txt", "r") as file :
        liste = file.readlines()
        longueur_liste = len(liste)
    
    #on prend un nombre aléatoire entre 0 et la longueur de la liste -1
    nummot = randint(0, longueur_liste-1)
    
    #on prend le mot de la liste correspondant au numéro
    mot = liste[nummot].strip()
    
    #si le mot est inférieur à 5 caractères on en prend un autre
    if len(mot) < 5 :
        return choix_mot()
    remplace
    #on renvoie le mot
    return mot



def initialisation(mot):
    mot_visible = ''
    
    #on met un underscore par caractère dans le mot à deviner
    for i in range(len(mot)):   
        mot_visible+='_'
    
    #on affiche la première lette du mot à afficher et toutes ses occurences dans le mot
    return remplacement_lettre(mot[0], mot, mot_visible)



def choix_lettre(mot, mot_visible, essais):
    #on demande une lettre au joueur
    lettre = input('Proposition de lettre : ').lower()

    #on vérifie que la lettre est dans le mot
    if lettre in mot:
        #si oui on la remplace dans le mot à afficher
        return (mot, remplacement_lettre(lettre, mot, mot_visible), essais)
    
    #sinon on retire un essai
    return (mot, mot_visible, tes_mauvais(essais))
    


def tes_mauvais(essais):
    #on verifie que le nombre d'essais n'est pas nul
    if essais == 0 :
        #si le nombre d'essai est nul on perd et on réinitialise le nombre d'essai
        perdu()
        return 8
    #on diminue de 1 le nombre d'essais restants
    return essais-1
    

def remplacement_lettre(lettre, mot, mot_visible):
    #on parcourt tout le mot à deviner
    for i in range(len(mot)):
        #si la lettre est dans le mot on le remplace dans le mot à afficher
        if mot[i] == lettre :
            caracteres = list(mot_visible)
            caracteres[i] = lettre
            mot_visible = ''.join(caracteres)
    return mot_visible


def verif_fini(mot_visible):
    #on verifie qu'il reste des lettres à trouver 
    if not '_' in mot_visible:
        #si non, on a gagné
        print('Bravo vous avez réussi à trouver le mot')
        return fin()
    #si oui on retourne dans pendu
    return 'yousk2'


def perdu():
    #t'es nul
    print('Tu es vraiment pas très bon, tu veux recommencer ? ')
    return fin()

def fin():
    #on propose au joueur de continuer
    reponse = input('Voulez-vous continuer à jouer ? Oui      Non    ').lower()
    reponse_valable = ['oui', 'o', 'yes', 'y', 'no','non','n']
    #on vérifie les réponses valables
    if reponse not in reponse_valable :
        #si la réponse n'est pas valable on redemande
        return fin()
    if reponse == 'no' or reponse =='n' or reponse == 'non' :
        #si la réponse est non on arrête
        print( "Merci d'avoir joué")
    else :
        #si la réponse est oui on continue
        return pendu()
        