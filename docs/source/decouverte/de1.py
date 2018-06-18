from microbit import *

import random

un = Image("00000:00000:00900:00000:00000")
deux = Image("00009:00000:00000:00000:90000")
trois = Image("90000:00000:00900:00000:00009")
quatre = Image("90009:00000:00000:00000:90009")
cinq = Image("90009:00000:00900:00000:90009")
six = Image("90009:00000:90009:00000:90009")

issues = [un, deux, trois, quatre, cinq, six]

while True:
    if button_a.get_presses():
        display.show(random.choice(issues))
        sleep(800)
        display.clear()