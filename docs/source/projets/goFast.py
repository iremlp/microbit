# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
# code utilisé pour l'atelier colloque C2i collège
# auteur : groupe InEFLP IREM de Marseille

from microbit import *
import random

# différente ETAT du jeu
# si etat == 0 : attente du début de partie (A ou B)
# si etat == 1 : compte à rebours
# si etat == 2 : en cours de partie
# si etat == 3 : affichage du gagnant
etat = 0

# victoire == "A" : bouton A gagne
# victoire == "B" : bouton B gagne
# victoire == "" : personne
victoire = ""

# fonction CHRONO qui sert de chronomètre
# retourne la durée écoulée depuis
# l'instant t0
t0 = running_time()

def chrono(t0):
    t1 = running_time()
    duree = t1-t0
    return duree

display.show(Image.HEART_SMALL)

while True:
    
    if etat == 0:
        if button_a.is_pressed() or button_b.is_pressed():
            # remise à zéro de la durée de la partie
            t0 = running_time()
            etat = 1
            sleep(250)

    # duree de la partie
    duree = chrono(t0)
    
    if etat == 1:        
        # si les joueurs sont trop pressés, ils perdent…
        if button_a.is_pressed():
            victoire = "B"
            etat = 3
        if button_b.is_pressed():
            victoire = "A"
            etat = 3
        
        # affichage du compte à rebours
        if duree < 1000:
            display.show("3")
        elif duree < 2000:
            display.show("2")
        elif duree < 3000:
            display.show("1")
        else:
            # initialisation d'une partie
            #
            # effacer écran
            display.clear()
            # attente et image aléatoire
            attente = duree + random.randint(500, 5000)
            imageAuHasard = random.choice(Image.ALL_CLOCKS)
            etat = 2
    
    if etat == 2:        
        # si les joueurs sont trop pressés, ils perdent…
        if duree < attente:
            if button_a.is_pressed():
                victoire = "B"
                etat = 3
            if button_b.is_pressed():
                victoire = "A"
                etat = 3
        
        # détermination du plus rapide des 2 joueurs
        if duree > attente:
            display.show(imageAuHasard)
            if button_a.is_pressed():
                victoire = "A"
                etat = 3
            if button_b.is_pressed():
                victoire = "B"
                etat = 3
    
    if etat == 3:
        # petite animation pour le suspens
        for i in range(5):
            display.show(Image.HEART_SMALL)
            sleep(100)
            display.show(Image.HEART)
            sleep(100)
        # affichage du gagnant
        if victoire == "A":
            display.show(Image.ARROW_W)
        if victoire == "B":
            display.show(Image.ARROW_E)
        etat = 0
    
    sleep(100)