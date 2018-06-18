from microbit import *

import random

piece1 = Image(           # définiton de l'image "piece1"
                "00000:"        # aucune diode n'est éclairée
                "00000:"
                "00000:"
                "99999:"        # toutes les diodes de la 4ème ligne sont éclairées au maximum
                "00000:")

piece2 = Image(
                "00000:"
                "90000:"
                "09000:"
                "00900:"
                "00090:")

piece3 = Image(
                "00000:"
                "00900:"
                "00900:"
                "00900:"
                "00900:")

piece4 = Image(
                "00000:"
                "00009:"
                "00090:"
                "00900:"
                "09000:")

piece5 = Image(
                "00000:"
                "00000:"
                "99999:"
                "00000:"
                "00000:")

while True:
    if button_a.get_presses():
        display.show(piece1)        # la matrice de LED montre l'image "piece1"
        sleep(200)
        display.show(piece2)
        sleep(200)
        display.show(piece3)
        sleep(200)
        display.show(piece4)
        sleep(200)
        display.show(piece5)
        sleep(200)
        display.show(piece1)
        sleep(200)
        display.show(random.choice(["P", "F"])) # affichage au hasard de P ou F
