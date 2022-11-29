import random

deckkleuren = ('Harten', 'Klaveren', 'Schoppen', 'Ruiten')
deckkaarten = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer', 'Aas')
deck = []

for i in range(13):
    deck.append(deckkleuren[0] + ' ' + deckkaarten[i])
    deck.append(deckkleuren[1] + ' ' + deckkaarten[i])
    deck.append(deckkleuren[2] + ' ' + deckkaarten[i])
    deck.append(deckkleuren[3] + ' ' + deckkaarten[i])
deck.append('Joker'), deck.append('Joker')
random.shuffle(deck)

for i in range(1, 8):
    firstseven = print(f'Kaarten {i}: {deck.pop()}')
print(f'''
[Deck] Kaarten: {len(deck)}
{deck}''')