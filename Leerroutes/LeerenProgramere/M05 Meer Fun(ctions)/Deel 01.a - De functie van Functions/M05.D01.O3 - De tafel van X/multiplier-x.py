def rekenen(nummer):
    string = ""
    for getal in range(1,11):
        string += f"{getal} x {nummer} = {getal * nummer}\n"
    return string
        

print(rekenen(int(input("Van welk getal wilt u de tafel zien? "))))