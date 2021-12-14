#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : prend l'entrée de l'utilisateur et renvoie si elle est correcte ou non

Qui l'a fait : Michel COURBIN, Gabriel PAULET-DUPRAT

Created on Tue Nov 23 11:32:54 2021

Que reste-t-il à faire ?
Oui
"""

# Importation de bibiliothèques nécessaires

import automate as auto


# Fonctions nécessaires au programme


# Programme principal
tableau_phrase_test = [
                       'le joli chat joue.', # phrase correcte
                       'le joli chat joue .', # phrase correcte
                       'la grosse souris verte mange jean.', # phrase correcte
                       'Jean joue.', # phrase incorrecte
                       'Jean mange Martin.', # phrase incorrecte
                       '.', # phrase incorrecte
                       "Jean mange le chat", # phrase incorrecte
                       'le joli chat joue', # phrase incorrecte
                       'la grosse souris verte mange le joli petite chat blanc.', # phrase incorrecte
                       'le joli chat'] # phrase incorrecte
                       
for phrase in tableau_phrase_test :
    phrase_split = auto.split(phrase)
    print(auto.syntaxe(phrase_split))



# Phrase de test : le joli chat joue. => Phrase correcte
# le => Phrase incorrecte
# le. => Phrase incorrecte
# le joli chat joue . => Phrase correcte
# le joli chat joue => Phrase incorrecte
# joue. => Phrase incorrecte
#   => Phrase incorrecte
# . => Phrase incorrecte