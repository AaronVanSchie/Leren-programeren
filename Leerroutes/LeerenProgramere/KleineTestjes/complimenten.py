import random

naam = input("Wat is uw naam? ")
aantal = int(input("Hoevaak mag ik het laten hooren? "))
niet_repeat = 0
for i in range(aantal):
    randomcompliment = random.randint(1,4)
    while niet_repeat == randomcompliment:
        randomcompliment = random.randint(1,4)
    if randomcompliment == 1:
        print(f"Jij bent goed bezig {naam}!")
    elif randomcompliment == 2:
        print(f"Ga zo door {naam}!")
    elif randomcompliment == 3:
        print(f"Stop vooral NIET {naam}!")
    else:
        print(f"Je bent super {naam}!")
    niet_repeat = randomcompliment