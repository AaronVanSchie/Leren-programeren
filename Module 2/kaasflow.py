kleur_kaas = input("Welke kleur is de kaas? ")
if kleur_kaas == "geel":
    gaten_kaas = input("zitten er gaten in de kaas? ")
    if gaten_kaas == "ja":
        duur = input("is de kaas belagelijk duur? ")
        if duur == "ja":
            print("Emmenthaler")
        else :
            print("Leerdammer")
    else :
        hard = input("is de kaas hard als steen? ")
        if hard == "ja":
            print("Parmigiano Reggiano")
        else : 
            print("GoudseKaas")
else :
    schimmel = input("Heeft de kaas blauwe schimmel? ")
    if schimmel == "ja" : 
        korst = input("Heeft de kaas een korst? ")
        if korst == "ja" :
            print("Blue de Rochbaron")
        else : 
            print("Foune d Ambert")
    else :
        korst2 = input("Heeft de kaas een korst? ")
        if korst2 == "ja" : 
            print("Camenbert")
        else :
            print("Mozzarella")
    