const kleuren = ["green", "red","purple","blue","black"];

function CheckColour(button){
    buttonkleur = button.style.backgroundColor
    nr=kleuren.indexOf(buttonkleur)
    document.getElementById(button).style.backgroundColor = kleuren[nr+1]
    if ((nr+1)==kleuren.length-1){
        document.getElementById(button).remove()
    }
}

for(let i = 1; i< 30 + 1; i++){
    const div = document.createElement("button");
    div.textContent = i
    div.style.backgroundColor = kleuren[0];
    div.setAttribute("onClick", "CheckColour(this)");
    container.appendChild(div)
}