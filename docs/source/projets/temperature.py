# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *

# définir mes images persos
# pour les lignes qui se colorent
image1 = Image(
    '00000:'
    '00000:'
    '00000:'
    '00000:'
    '99999')    
image2 = Image(
    '00000:'
    '00000:'
    '00000:'
    '99999:'
    '77777')
image3 = Image(
    '00000:'
    '00000:'
    '99999:'
    '77777:'
    '77777')
image4 = Image(
    '00000:'
    '99999:'
    '77777:'
    '77777:'
    '77777')
image5 = Image(
    '99999:'
    '77777:'
    '77777:'
    '77777:'
    '77777')

# booléen pour savoir si l'énigme est réussie
victoire = False

# à faire toujours et toujours…
while True:
    # utiliser le bouton A pour réinitialiser
    if button_a.is_pressed():
        victoire = False
    
    # si l'énigme est résolue
    if victoire:
        # petite image joyeuse
        display.show(Image.HAPPY)
        sleep(500)
        # code secret à afficher…
        display.scroll("XXXXXX")
    
    # si  l'énigme n'a pas été résolue
    if not victoire:
        # lire la température (en °C)
        temp = temperature()
        # affichage des images en fonction
        # de temp
        if temp < 29:
            display.clear()
        elif 29 <= temp < 30:
            display.show(image1)
        elif 30 <= temp < 31:
            display.show(image2)
        elif 31 <= temp < 32:
            display.show(image3)
        elif 32 <= temp < 33:
            display.show(image4)
        elif 33 <= temp < 34:
            display.show(image5)
        # victoire !
        elif 34 <= temp:
            victoire = True
            # petite animation
            for i in range(2):
                display.show(Image.SQUARE_SMALL)
                sleep(100)
                display.show(Image.SQUARE)
                sleep(100)
        sleep(500)