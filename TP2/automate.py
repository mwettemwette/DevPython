    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : regroupe toutes les fonctions utiles pour vérifier qu'une phrase est correcte

Qui l'a fait : Michel COURBIN, Gabriel PAULET-DUPRAT

Created on Tue Nov 23 10:34:11 2021

Que reste-t-il à faire ?
Oui
"""
def phrase_correcte(): 
    # vérifie que la phrase est correcte
    
    phrase = input("Entrez la phrase : ") # l'utilisateur rentre manuellement sa phrase
    phrase_split = split(phrase) # on utilise la fonction split pour la découper
    print(syntaxe(phrase_split)) # affiche si la phrase est correcte ou pas


def recup_dictionnaire():
    # crée un dictionnaire à partir d'un fichier texte
    
    dictionnaire = {}
    for ligne in open("dictionnaire.txt",'r') :
        ligne_split = ligne.split()
        dictionnaire[ligne_split[0]] = int(ligne_split[1])
    return dictionnaire

dictionnaire = recup_dictionnaire() # création du dictionnaire


def syntaxe(phrase_split): 
    # vérifie que la phrase est correcte et l'affiche à l'utilisateur
    
    etat=0
    for mot in phrase_split :
        etat = verif(mot, etat)
    if etat == 9 :
        return 'Phrase correcte'
    return 'Phrase incorrecte'


def split(phrase):
    # découpe la phrase en mots et décolle le point s'il est collé au dernier mot
    
    if phrase[-1] != '.' or phrase == '.':
        return [' ']
    if phrase[-2] != ' ' :
        phrase = phrase[:-1] + ' .'
    return phrase.split()


def verif(mot,etat):
    # vérifie si le mot est répertorié dans le dictionnaire ou non et vérifie qu'il suit la table de transition en fonction de l'état
    
    table_transition = [[1,8,8,8,4,8],
                        [8,1,2,8,8,8],
                        [8,2,8,3,8,8],
                        [5,8,8,8,7,9],
                        [8,8,8,3,8,8],
                        [8,5,6,8,8,8],
                        [8,6,8,8,8,9],
                        [8,8,8,8,8,9],
                        [8,8,8,8,8,8],
                        [8,8,8,8,8,8]]
    if mot not in dictionnaire :
        return 8 
    return table_transition[etat][dictionnaire[mot]]
