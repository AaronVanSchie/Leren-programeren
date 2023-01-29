print(f'''
{"-" * 20}
| Locatie : Rotterdam
| Postcode : 5876 KA
| Email : SolicitatieRotterdam@gmail.com
{"-" * 20}''')
naam = input("Wat is uw naam? ")
dieren = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
acrobatiek = int(input("Hoeveel jaar praktijkervating heeft u met acrobatiek? "))
diploma = input("Heeft u een MBO-4 diploma onderneming? J/N ") == "J"
vrachtwagen = input("Bent u in bezit van een gelding vrachtwagen rijbewijs? J/N ") == "J"
hoed = input("Heeft u een hoge hoed? J/N ") == "J"
geslacht = input("Bent u een man of vrouw? M/V ")
if geslacht == "M":
   lsnor = int(input("Hoe breed is uw snor in cm? "))
elif geslacht == "V":
    roodhaar = input("Is uw haar rood? J/N ") == "J"
    lhaar = int(input("Hoelang is uw haar in cm? "))
lengte = int(input("Wat is uw lengte in cm? "))
gewicht = int(input("Wat is uw lichaamsgewicht in kg? "))
certificaat = input("Bent u in bezit van een cerificaat voor werken met gevaarlijk personeel? J/N ") == "J"
hoogte = input("Heeft u hoogtevrees? J/N ") == "N"
jett = input("Can jett revive jou? J/N ") == "J"
douche = int(input("Hoevaak per week douched u? "))
discord = input("Gebruikt u discord? J/N ")
if dieren >= 3 and jongleren >= 4 and acrobatiek >= 5 and diploma and vrachtwagen and hoed and (geslacht == "M" and lsnor >=10 or geslacht == "V" and roodhaar and lhaar >= 20) and lengte and gewicht and certificaat and hoogte and jett and douche >= 7 and discord :
    print(f'''
    Gefeliciteerd {naam}
    u bent geschikt voor deze baan! ''')
else:
    print(f'''
    Beste {naam} 
    u bent helaas niet geschikt voor deze baan.''')