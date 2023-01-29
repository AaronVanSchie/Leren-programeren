def addition():
    uitkomst = n1 + n2
    return uitkomst

def substraction():
    uitkomst = n1 - n2
    return uitkomst

def multiplication():
    uitkomst = n1 * n2
    return uitkomst

def division():
    uitkomst = n1 / n2
    return uitkomst

repeat = True
while repeat == True:
    uitkomst = 0
    choice = input("wat wilt u doen?\nA) getallen optellen,\nB) getallen aftrekken,\nC) getallen vermenigvuldigen,\nD) getallen delen,\nE) getal ophogen,\nF) getal verlagen,\nG) getal verdubbelen,\nH) getal halveren\n: ").upper()

    if choice == "A" or choice == "B" or choice == "C" or choice == "D":
        n1 = float(input("Kies een getal: "))
        n2 = float(input("Kies een getal: "))
    elif choice == "E" or choice == "F":
        n1 = float(input("Kies een getal: "))
        n2 = 1
    else:
        n1 = 2
        n2 = float(input("Kies een getal: "))

    if choice == "A" or choice == "E":
        uitkomst += addition()
    elif choice == "B" or choice == "F":
        uitkomst += substraction()
    elif choice == "C" or choice == "G":
        uitkomst += multiplication()
    elif choice == "D" or choice == "H":
        uitkomst += division()

    choice2 = input(f"Wil je wat met de uitkomst {uitkomst} doen? J/N ").upper()
    if choice2  == "J":
        repeat = True
        print()
    elif choice2 == "N":
        repeat = False
