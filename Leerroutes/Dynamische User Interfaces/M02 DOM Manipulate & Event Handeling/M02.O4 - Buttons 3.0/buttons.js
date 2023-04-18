kleuren = ["green","red","purple","blue","black"];

function colorchange(button){
    buttonkleur = document.getElementById(button).style.backgroundColor
    nmbr = kleuren.indexOf(buttonkleur)
    document.getElementById(button).style.backgroundColor = kleuren[nmbr +1]
    if (nmbr + 1 == kleuren.length){
        document.getElementById(button).remove()
    }
}

for(let i = 1; i< 30 + 1; i++){
    var div = document.createElement('button');
    div.style.backgroundColor= kleuren[0]
    div.setAttribute("id", i)
    div.setAttribute("onclick", "colorchange("+ i +")")
    div.textContent = i
    container.appendChild(div)
}
