let vraag = prompt("Wat wilt u bestellen:")

let fris = 0
let wijn = 0
let bier = 0

let fris_prijs = 3
let wijn_prijs = 12
let bier_prijs = 4


while (vraag != "nee"){
    if (vraag != "fris" & vraag != "wijn" & vraag !=  "bier" & vraag != "stop"){
        alert("dit ken ik niet")
    } if (vraag == "fris" || vraag == "wijn" || vraag == "bier" ) {    
        let hoeveel = Number(prompt("Hoeveel wilt u hier van:"))
        if (vraag == "fris"){
            fris += hoeveel
        }  if (vraag == "wijn"){
            wijn += hoeveel
        }  if (vraag == "bier"){
            bier += hoeveel
        }
    } 
    vraag = prompt("Wat wilt u bestellen:")
}

if (fris > 0){
    document.write("<br>", "Fris ", ' '.repeat(10), fris, " €", fris_prijs * fris)
} if (wijn > 0){
    document.write("<br>", "Wijn ", wijn, " €", wijn_prijs * wijn)
} if (bier > 0){
    document.write("<br>", "Bier ", bier, " €", bier_prijs * bier)
}

document.write("<br>" + "<br>" + "Dit word bij elkaar €", (fris_prijs * fris) + (wijn_prijs * wijn) + (bier_prijs * bier))