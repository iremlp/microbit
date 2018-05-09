from microbit import *
from random import random, seed

seed(300)               # la graine de hasard ???
n = [0, 0, 0, 0, 0]     # le tableau contenant les compteurs


def aff(n, m):          # la fonction affichant le graph
    q = n // 9          # nombre de led eclaire totalement
    r = n % 9           # portion de la derniere led eclaire
    for i in range(0, q):
        display.set_pixel(m, 4-i, 9)
    display.set_pixel(m, 4-q, r)


def chute(t):                # fonction affichant la chute
    display.clear()
    y, x = 0, 0
    display.set_pixel(x, y, 9)
    sleep(t)
    while y < 4:
        display.clear()
        if round(random()):      # si arrondi de alea est vrai (différent de 0)
            y = y + 1            # on augmente y de 1
        else:
            x = x + 1
            y = y + 1
        display.set_pixel(x, y, 9)
        sleep(t)
    n[x] = n[x]+1        # incrementation du compteur de la position x
    display.set_pixel(x, y, 1)


while True:
    if button_a.is_pressed():
        chute(500)

    elif button_b.get_presses():
        n = [0, 0, 0, 0, 0]
        for k in range(80):
            chute(round(500 / (1.05**k)))
            for j in range(5):
                aff(n[j], j)
            sleep(200)
        print(n)
