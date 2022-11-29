itemList = {}
userInput = input('Wilt u wat toevoegen aan het boodschappenlijstje? J/N ').lower()

while not userInput != 'j':
    itemName = str(input('Wat wilt u toevoegen aan het boodschappenlijstje? ')).capitalize()
    itemAmount = int(input(f'Hoeveel wilt u toevoegen van {itemName}? '))
    if itemName in itemList:
        itemList[itemName] += itemAmount
    else:
        itemList[itemName] = itemAmount
    userInput = input('Wilt u wat toevoegen aan het boodschappenlijstje? J/N ').lower()

print(f'[ BOODSCHAPPENLIJSTJE ]')
for itemName in itemList:
    amountString = str(itemList[itemName])
    print(f"{amountString} x {itemName}")