kleur_kaas = input("Welke kleur is de kaas? ")
if kleur_kaas.lower() == "geel" :
    gaten_kaas = input("zitten er gaten in de kaas? ")
    if gaten_kaas .lower() == "ja":
        duur = input("is de kaas belagelijk duur? ")
        if duur .lower() == "ja":
            print("Emmenthaler")
        else :
            print("Leerdammer")
    else :
        hard = input("is de kaas hard als steen? ")
        if hard .lower() == "ja":
            print("Parmigiano Reggiano")
        else : 
            print("GoudseKaas")
elif kleur_kaas.lower() == "wit" :
    print("brie")
else :
    schimmel = input("Heeft de kaas blauwe schimmel? ")
    if schimmel .lower() == "ja" : 
        korst = input("Heeft de kaas een korst? ")
        if korst .lower() == "ja" :
            print("Blue de Rochbaron")
        else : 
            print("Foune d Ambert")
    else :
        korst2 = input("Heeft de kaas een korst? ")
        if korst2.lower() == "ja" : 
            print("Camenbert")
        else :
            print("Mozzarella")
