try:
    iphone = float(input("Hoe duur is de iPhone 13: "))
    samsung = float(input("Hoe duur is de Samsung Galaxy S22: "))
    asus = float(input("Hoe duur is de Asus Zenfone 9: "))
except ValueError:
    print("Dit is niet mogelijk probeer opnieuw!")
iphoneverschilsamsung = iphone - samsung
iphoneverschilasus = iphone - asus
samsungverschilasus = samsung - asus
samsungverschiliphone = samsung - iphone
asusverschiliphone = asus - iphone 
asusverschilsamsung = asus - samsung

print()

if iphone > samsung and iphone > asus and samsung < asus:
    print(f"De iPhone 13 is het duurst, de telefoon  kost: {iphone} Euro.")
    print(f"De Samsung Galaxy S22 is het goedkoopst, de telefoon kost {samsung} Euro.")
    print(f"De Asus Zenfone 9 zit er tussenin met: {asus} Euro") 
elif iphone > samsung and iphone > asus and samsung > asus:
    print(f"De iPhone 13 is het duurst, de telefoon  kost: {iphone} Euro.")
    print(f"De Asus Zenfone 9 is het goedkoopst, de telefoon kost {asus} Euro.")
    print(f"De Samsung Galaxy S22 zit er tussenin met: {samsung} Euro") 
elif iphone < samsung and asus < samsung and iphone < asus:
    print(f"De Samsung Galaxy S22 is het duurst, de telefoon  kost: {samsung} Euro.")
    print(f"De iPhone 13 is het goedkoopst, de telefoon kost {iphone} Euro.")
    print(f"De Asus Zenfone 9 zit er tussenin met: {asus} Euro")
elif iphone < samsung and asus < samsung and iphone > asus:
    print(f"De Samsung Galaxy S22 is het duurst, de telefoon  kost: {samsung} Euro.")
    print(f"De Asus Zenfone 9 is het goedkoopst, de telefoon kost {asus} Euro.")
    print(f"De iPhone 13 zit er tussenin met: {iphone} Euro")
elif asus > iphone and asus > samsung and iphone > samsung:
    print(f"De Asus Zenfone 9 is het duurst, de telefoon  kost: {asus} Euro.")
    print(f"De iPhone 13 is het goedkoopst, de telefoon kost {iphone} Euro.")
    print(f"De Samsung Galaxy S22 zit er tussenin met: {samsung} Euro")
elif asus > iphone and asus > samsung and iphone < samsung:
    print(f"De Asus Zenfone 9 is het duurst, de telefoon  kost: {asus} Euro.")
    print(f"De Samsung Galaxy S22 is het goedkoopst, de telefoon kost {samsung} Euro.")
    print(f"De iPhone 13 zit er tussenin met: {iphone} Euro")
elif asus == samsung == iphone:
    print("Alle telefoons zijn even duur.")

print()

if samsungverschilasus > 100 and iphoneverschilasus > 100:
    print(f'''
Het advies is om de Asus Zenfone 9 te kopen
Deze is namelijk 100 Euro goedkoper/duurder dan de iPhone 13 
En 100 Euro goedkoper/duurder dan de Samsung Galaxy S22
''')
elif iphone <= 50 + samsung:
    print(f"Het advies is de iPhone 13 te kopen. Deze is namelijk {iphoneverschilsamsung} goedkoper/duurder dan de Samsung Galaxy S22 en {iphoneverschilasus} goedkoper/duurder dan de Asus Zenfone 9.")
    print()
elif iphone >= 900 or samsung >= 900:
    print("Het advies is dus om geen telefoon te kopen, ze zijn te duur.")
    print()
else:
    print(f"Het advies is de Samsung Galaxy S22 te kopen. Deze is namelijk {samsungverschiliphone} goedkoper/duurder dan de iPhone 13 en {samsungverschilasus} goedkoper/duurder dan de Asus Zenfone 9.")
    print()

