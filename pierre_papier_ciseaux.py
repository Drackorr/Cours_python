# pierre, papier, ciseaux ameliorer

from random import randint
import os
import time  # on importe ce module pour interompre l'exécution aux points-clés

# Creation de mes cartes, combinner a une valeur numerique
rock = 1
paper = 2
scissors = 3

# On fixe les régles du jeu, ainsi que le nom en chaine de caractère de chaque variable.
names = {rock: "pierre", paper:"papier", scissors:"ciseaux"}
rules = {rock:scissors,paper:rock, scissors:paper}  # on définit les régles ici, quelle variable est supérieure à l'autre.

# Definition de la première fonctions

def start():
    print("Nous allons jouer à pierre, papier, ciseaux version ameliorer!")   # On annonce le jeu
    while game():    # On crée une première boucle avec la fonction "game", définie plus loin.
        pass         # Pass permet d'arrêter le jeu une fois que nous avons fini.

# Decoupage des differents module du jeu

def nbre_class(): # nombre de personne dans la classes qui choissisent une carte "ici de façon aleatoire"


