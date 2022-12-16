# name of student: Aaron van Schie
# number of student: 99071407
# purpose of program: Wissel geld terug krijgen zonder zelf te bereken
# function of program: Niet zelf wisselgeld hoeven te bereken
# structure of program: bad

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay # Snelle berekening om te zien wat het wissel geld is/word
returned = {}

if change > 0: # Als change groter is dan 0 moet er wat betaald worden
  coinValue = 500 # De coinvalue in cents is hier 50
  
  while change > 0 and coinValue > 0: # een loop terwijl change en coinvalue grooter zijn dan 0
    nrCoins = change // coinValue # aantal coins gedeelt door coinvalue

    if nrCoins > 0: # als aantal coins groter is dan 0 doet hij het volgende
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # hier zie je hoeveel coins je van de coinvalue moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # een variabele die laat zien hoeveel je coins wisselgeld hebt gegeven
      change -= nrCoinsReturned * coinValue # een snelle berekening dat laat zien hoeveel change er al gegeven is
      returned[coinValue] = nrCoinsReturned
# comment on code below: als de coinvalue gelijk is aan bv 50 dan gebruikt hij 20 coinvalue
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

print(returned)

if change > 0: # dit doet hij als change NOGSTEEDS groter is dan 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')