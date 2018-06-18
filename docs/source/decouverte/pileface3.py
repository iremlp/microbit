from microbit import *

import random

p = 0           # variable stockant le nombre d'issues pile
f = 0           # variable stockant le nombre d'issues face

piece1 = Image("00000:"
               "00000:"
               "00000:"
               "99999:"
               "00000:")

piece2 = Image("00000:"
               "90000:"
               "09000:"
               "00900:"
               "00090:")

piece3 = Image("00000:"
               "00900:"
               "00900:"
               "00900:"
               "00900:")

piece4 = Image("00000:"
               "00009:"
               "00090:"
               "00900:"
               "09000:")

piece5 = Image("00000:"
               "00000:"
               "99999:"
               "00000:"
               "00000:")

pieces = [piece1, piece2, piece3, piece4, piece5, piece1]

while True:
    if button_a.get_presses():
        display.show(pieces, delay=200)
        issue = random.choice(["P", "F"])
        if issue == "P":
            display.show("P")
            p += 1                          # incrémentation de la variable p (pile)
        else:
            display.show("F")
            f += 1                          # incrémentation de la variable f (face)

    if button_b.get_presses():
        display.scroll("P:"+str(p))     # affichage du nombre d'issues associées à P
        delay = 200
        display.scroll("F:"+str(f))     # affichage du nombre d'issues associées à F
