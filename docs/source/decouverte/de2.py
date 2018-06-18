from microbit import *

import random

un = Image("00000:00000:00900:00000:00000")
deux = Image("00009:00000:00000:00000:90000")
trois = Image("90000:00000:00900:00000:00009")
quatre = Image("90009:00000:00000:00000:90009")
cinq = Image("90009:00000:00900:00000:90009")
six = Image("90009:00000:90009:00000:90009")

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

issues = [un, deux, trois, quatre, cinq, six]

while True:
    if button_a.get_presses():
        issue = random.choice(issues)
        display.show(issue)
        if issue == un:
            n1 += 1
        elif issue == deux:
            n2 += 2
        elif issue == trois:
            n3 += 1
        elif issue == quatre:
            n4 += 1
        elif issue == cinq:
            n5 += 1
        elif issue == six:
            n6 += 1
        sleep(1000)
        display.clear()
    
    if button_b.get_presses():
        display.scroll(
            str(n1)+" /"+str(n2)+" /"
            + str(n3)+" /"+str(n4)+" /"
            + str(n5)+" /"+str(n6)
            )