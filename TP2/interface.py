#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Header

"""
Que fait ce programme : prend l'entrée de l'utilisateur et renvoie si elle est correcte ou non

Qui l'a fait : Michel COURBIN, Gabriel PAULET-DUPRAT

Created on Tue Nov 23 08:04:06 2021

Que reste-t-il à faire ?
Oui
"""

# Importation de bibiliothèques nécessaires

import automate as auto


# Fonctions nécessaires au programme


# Programme principal

auto.phrase_correcte()


# Phrase de test : le joli chat joue. => Phrase correcte
# le => Phrase incorrecte
# le. => Phrase incorrecte
# le joli chat joue . => Phrase correcte
# le joli chat joue => Phrase incorrecte
# joue. => Phrase incorrecte
#   => Phrase incorrecte
# . => Phrase incorrecte