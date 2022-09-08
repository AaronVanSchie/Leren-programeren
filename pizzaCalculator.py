# Aaron van Schie  opdracht: PizzaCalculator
small = int(input("Aantal pizza`s small:"))
medium = int(input("Aantal pizza`s medium:"))
large = int(input("Aantal pizza`s large:"))
psmall = 3
pmedium = 6 
plarge = 11
print(f'''
Aantal bestelde pizza`s
Small: {small}
Medium: {medium}
Large: {large}
Totaal prijs:
{small * psmall + medium * pmedium + large * plarge} Euro
''')