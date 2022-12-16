import random 

kleuren = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
hoeveelheid = int(input("Hoeveel M&M`s wilt u in de zak hebben? "))
zak = {}
for x in range(hoeveelheid+5):
    randomkleur = random.choice(kleuren)
    if randomkleur == "Rood":
        if "Rood" not in zak:
            zak.update({"Rood" : 0})
        else:
            zak["Rood"] += 1
    if randomkleur == "Blauw":
        if "Blauw" not in zak:
            zak.update({"Blauw" : 0})
        else:
            zak["Blauw"] += 1
    if randomkleur == "Groen":
        if "Groen" not in zak:
            zak.update({"Groen" : 0})
        else:
            zak["Groen"] += 1
    if randomkleur == "Geel":
        if "Geel" not in zak:
            zak.update({"Geel" : 0})
        else:
            zak["Geel"] += 1
    if randomkleur == "Bruin":
        if "Bruin" not in zak:
            zak.update({"Bruin" : 0})
        else:
            zak["Bruin"] += 1
if "Rood" == 0:
    zak.pop([1])
elif "Blauw" == 0:
    zak.pop([2])
elif "Groen" == 0:
    zak.pop([3])
elif "Geel" == 0:
    zak.pop([4])
elif "Bruin" == 0:
    zak.pop([5])
print(zak)