let vraag = prompt("Wat wilt u bestellen:")

if (vraag != "fris" || "wijn" || "bier" || "stop"){
    console.log("dit ken ik niet")
} else if (vraag == "stop") {
    console.log("GESTOPT")
} else if (vraag == "fris" || "wijn" || "bier" ) {    
    let hoeveel = Number(prompt("Hoeveel wilt u hier van:"))
    console.log(vraag, hoeveel)
}
