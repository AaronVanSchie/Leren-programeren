try:
    iphone = float(input("Hoe duur is de iPhone 13: "))
    samsung = float(input("Hoe duur is de Samsung Galaxy S22: "))
except ValueError:
    print("Dit is niet mogelijk probeer opnieuw!")
verschil = iphone - samsung

if iphone > samsung:
    print(f"De iPhone 13 is het duurst, de telefoon  kost: {iphone} Euro.")
    print(f"De Samsung Galaxy S22 is het goedkoopst, de telefoon kost {samsung} Euro.")
elif iphone < samsung: 
    print(f"De Samsung Galaxy S22 is het duurst, de telefoon  kost: {samsung} Euro.")
    print(f"De iPhone 13 is het goedkoopst, de telefoon kost {iphone} Euro.")
else:
    print("Bijde telefoons zijn even duur.")

if iphone == 50 + samsung:
    print(f"Het advies is dus om de iPhone 13 te kopen Deze is namelijk {verschil} Euro goedkoper/duurder dan de Samsung Galaxy S22")
    print()
else:
    print(f"Het advies is dus om de Samsung Galaxy S22 te kopen Deze is namelijk {verschil} Euro goedkoper/duurder dan de iPhone 13")
    print()