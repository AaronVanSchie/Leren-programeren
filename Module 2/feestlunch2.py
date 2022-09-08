Croisants = int(input("Aantal croisants:"))
Stuksprijs = 39
Stokbroden = int(input("Aantal Stokbroden:"))
Prijs = 278
Kortings = int(input("Aantal Kortings bonnen:"))
Korting = 50
print(f'''
De door u samengestelde lunch kost:
{Croisants * Stuksprijs + Stokbroden * Prijs - Kortings * Korting} Cent''')