from microbit import *

import random

piece1 = Image(
                "00000:"
                "00000:"
                "00000:"
                "99999:"
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

pieces = [piece1, piece2, piece3, piece4, piece5, piece1]   # la séquence d'images

while True:
    if button_a.get_presses():
        display.show(pieces, delay=200)             # la matrice affiche chacune des images de la liste "pieces" avec une pause de 200ms entre chaque image
        display.show(random.choice(["P", "F"]))
