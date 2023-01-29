totaalscore = 0

naamstudent = input("Naam Student: ")
achternaamstudent = input("Achternaam student: ")
studentcode = int(input("Student code: "))
naammentor = input("Naam mentor: ")
achternaammentor = input("Achternaam mentor: ")

while True:
    try:
        scoreE = int(input("Hoeveel punten wilt u de leerling geven voor het onderdeel excellente acties? "))
    except ValueError : print("Dit is geen correct getal!")
    if scoreE <=6 :
        puntenE =  input(f"Wilt u {naamstudent} {scoreE} punten geven? J/N ")
        break
    else:
        print(f"u kund {naamstudent} niet {scoreE} aantal punten geven. ")
        print("")
totaalscore = totaalscore + scoreE

while True:
    try:
        scoreP = int(input("Hoeveel punten wilt u de leerling geven voor het onderdeel professionele acties? "))
    except ValueError : print("Dit is geen correct getal!")
    if scoreP <=8 :
        puntenP =  input(f"Wilt u {naamstudent} {scoreP} punten geven? J/N ")
        break   
    else:
        print(f"u kund {naamstudent} niet {scoreP} aantal punten geven. ")
        print("")
totaalscore = totaalscore + scoreP

while True:
    try:
        scoreO = int(input("Hoeveel punten wilt u de leerling geven voor het onderdeel onprofessionele acties? "))
    except ValueError : print("Dit is geen correct getal!")
    if scoreO <=5 :
        puntenO =  input(f"Wilt u {naamstudent} {scoreO} punten geven? J/N ")     
        break
    else:
        print(f"u kund {naamstudent} niet {scoreO} aantal punten geven. ")
        print("")
totaalscore = totaalscore + scoreO

while True:
    try:
        scoreS = int(input("Hoeveel punten wilt u de leerling geven voor het onderdeel slechte acties? "))
    except ValueError : print("Dit is geen correct getal!")
    if scoreS <=2 :
        puntenS=  input(f"Wilt u {naamstudent} {scoreS} punten geven? J/N ")     
        break
    else:
        print(f"u kund {naamstudent} niet {scoreS} aantal punten geven. ")
        print("")
totaalscore = totaalscore + scoreS

if scoreE >4 and scoreP == 8 and scoreO == 0 and scoreS == 0:
    scoreGoed = True 
    score =  "Goed"
elif (scoreE + scoreP - scoreO == 8 and scoreS == 0) or (scoreS == 1 and scoreE + scoreP - scoreO >9):
    scoreVoldoende = True
    score = "Voldoende"
else :
    scoreOnvoldoende = True
    score = "Onvoldoende"

print(f'''
|{"+" * 40}
| Examen resultatem
|{"-" * 40}
| Naam student : {naamstudent} {achternaamstudent}
| Studentecode : {studentcode}
| Naam mentor : {naammentor} {achternaammentor}
|{"-" * 40}
| Excellente acties : {scoreE}
| Professionele acties : {scoreP}
| Onprofessionele acties : {scoreO}
| Slecht acties : {scoreS}
|{"-" * 40}
| Totaal score : {totaalscore}
| Score : {score}
|{"+" * 40}
''')
print(" ")