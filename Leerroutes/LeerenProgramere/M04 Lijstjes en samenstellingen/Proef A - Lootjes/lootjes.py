import random

namen = []
lootjes = []
aantal_namen = int(input("Hoeveel mensen doen er mee? "))

while aantal_namen < 3:
    if aantal_namen < 3:
        print("Dit is niet mogelijk probeer opnieuw")
    aantal_namen = int(input("Hoeveel mensen doen er mee? "))

i = 0

while i != aantal_namen:
    naam = input("Voor een naam in: ")
    if naam not in namen:
        namen.append(naam)
        lootjes.append(naam)
        i += 1
    else:
        print("Deze naam is niet uniek! Probeer opnieuw")

random.shuffle(lootjes)
Repeat_Shuffel = False

while not Repeat_Shuffel:
    random.shuffle(lootjes)
    Repeat_Shuffel = True
    for x in range(0,len(lootjes)):
        if namen[x] == lootjes[x]:
            Repeat_Shuffel = False
for x in range(0,len(lootjes)):
    print(f'{namen[x]} heeft {lootjes[x]} getroken')
