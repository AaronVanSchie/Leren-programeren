import random
import time

rounds = 0
kansen = 0
punten = 0
while rounds != 20:
    randomgetal = random.randint(0,1000)
    print(randomgetal)
    while kansen != 10:
        gegoktegetal = int(input("Kies een getal tussen 0/1000: "))
        gegokt = randomgetal - gegoktegetal
        if gegokt < 20 and gegokt > 0:
            print("Je bent heel warm!")
        elif gegokt > 20 and gegokt < 50:
            print("Je bent warm!")
        elif gegoktegetal == randomgetal:
            print()
            print("Goed gedaan dit was het juiste andwoord!")
            print()
            punten += 1
            break
        kansen += 1
        print()
        print(f"u heeft nog {10 - kansen} kansen")
        print()
        time.sleep(0.5)
        if kansen == 10:
            print(f"Het andwoord was {randomgetal}")
    stoppen = input("Wilt u stoppen? ").lower()
    if stoppen == "ja":
        exit()
    kansen -= kansen
    rounds += 1
    print()
    print(f"U heeft op het moment {punten} aantal punten")
    print(f"Dit was round {rounds}")
    print()