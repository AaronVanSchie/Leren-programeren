weekdagen = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag")
weekenddagen = ("Zaterdag", "Zondag")
heleweekdagen = weekdagen + weekenddagen

print(f"Alle dagen van de week zijn {weekdagen + weekenddagen}")
print(f"Alle werkdagen van de week zijn {weekdagen}")
print(f"Alle dagen van het weekend zijn {weekenddagen}")
print()
print("Alle dagen van de week omgekeerd zijn")
for i in range(1,8):
    print(heleweekdagen[-i])
print()
print("Alle werkdagen van de week omgedraait zijn")
for x in range(1,6):
    print(weekdagen[-x])
print()
print("Alle dagen van het weekend omgedraait zijn")
for y in range(1,3):
    print(weekenddagen[-y])