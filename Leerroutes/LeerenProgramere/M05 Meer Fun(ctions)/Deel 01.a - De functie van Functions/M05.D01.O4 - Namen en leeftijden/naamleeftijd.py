def name_age(i: list):
    name_input = input("Wat is de naam? ")
    leeftijd_input = input("Wat is de leeftijd? ")
    naam_leeftijd.append({
        "Naam": name_input,
        "Age": leeftijd_input
    })


naam_leeftijd = []
stoppen = False

while stoppen != True:
    name_age(naam_leeftijd)
    stop = input("Wilt u stoppen? (In hoofdletters!!) J/N ")
    if stop == "J":
        stoppen = True

for item in naam_leeftijd:
    print(item)
