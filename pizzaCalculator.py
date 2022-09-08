# Aaron van Schie  opdracht: PizzaCalculator
from tkinter import N


print("Hoeveel small pizzas?")
small = int(input())
print("Hoeveel medium pizzas?")
medium = int(input())
print("Hoeveel Large pizzas?")
large = int(input())
psmall = 3
pmedium = 6 
plarge = 11
print(f'''
{"-" * 20 } 
| Aantal bestelde pizza`s:
| Small: {small}
| Medium: {medium}
| Large: {large}
{"-" * 20}
Totaal prijs:
{small * psmall + medium * pmedium + large * plarge} Euro
''')