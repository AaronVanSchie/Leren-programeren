
prijssmall = 3 # Prijs kleine pizza
prijsmedium = 6 # Prijs medium pizza
prijslarge = 11 # Prijs grote pizza
while True:
    try:
        pizzasmall = int(input("Hoeveel small pizzas? "))
    except ValueError:
        print("Dit kan helaas niet!")
        print("")
    else:
        break
while True:
    try:
        pizzamedium = int(input("Hoeveel medium pizzas? "))
    except ValueError:
        print("Dit kan helaas niet!")
        print("")
    else:
        break
while True:
    try:
        pizzalarge = int(input("Hoeveel Large pizzas? "))
    except ValueError:
        print("Dit kan helaas niet!")
        print("")
    else:
        break
totaalprijs = (pizzasmall) * prijssmall + (pizzamedium) * prijsmedium + (pizzalarge) * prijslarge
print(f'''
|{"-" * 50}
| Locatie = Strijen
| Bedrijf = van Hooi
| Postcode = 3280 KA
|{"-" * 50}
| Aantal kleine Pizza : {pizzasmall}
| Aantal medium Pizza : {pizzamedium}
| Aantal groote Pizza : {pizzalarge}
|{"-" * 50}
| Totaal prijs :
| {totaalprijs} Euro
|{"-" * 50}
|ik wens u nog een fijne dag
|{"-" * 50}
''')