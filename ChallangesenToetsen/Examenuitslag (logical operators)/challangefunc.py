
def Numbercheck(vraag: str)-> int:
    try:
        aantal = int(input(vraag))
    except ValueError:
        print("Dit is geen correct getal!")
        return Numbercheck(vraag)
    return aantal

scoreE = Numbercheck("Hoeveel punten voor scoreE? ")
scoreP = Numbercheck("Hoeveel punten voor scoreP? ")
scoreO = Numbercheck("Hoeveel punten voor scoreO? ")
scoreS = Numbercheck("Hoeveel punten voor scoreS? ")

if scoreE >4 and scoreP == 8 and scoreO == 0 and scoreS == 0:
    scoreGoed = True 
    score =  "Goed"
elif (scoreE + scoreP - scoreO == 8 and scoreS == 0) or (scoreS == 1 and scoreE + scoreP - scoreO >9):
    scoreVoldoende = True
    score = "Voldoende"
else :
    scoreOnvoldoende = True
    score = "Onvoldoende"

print(f"u heeft een {score}")