import random

kleuren = ("Oranje","Blauw", "Groen", "Bruin")
hoeveelheid = int(input("Hoeveel M&M's moeten er in de zak? "))
zak = []
for willekeurig in range(1,hoeveelheid+1):
    randomkleur = random.choices(kleuren)
    zak.append(randomkleur)
print(zak)
