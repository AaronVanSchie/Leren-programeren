function changeImage(getal){
    reset();
    const container = document.getElementById("container");
    container.style.backgroundImage = "url(images/bg"+getal+".jpg)";
    const picture = document.getElementById("picture");
    picture.src = "images/"+getal+".jpg";
    document.getElementById(getal).innerHTML = Number(document.getElementById(getal).innerHTML) + 1;
    document.getElementById(getal).style.backgroundColor = "red"
    document.getElementById(getal).disabled = true;
}

function reset(){
    for (let i = 1; i < 4; i++){
        document.getElementById(i).style.backgroundColor = "#4CAF50";
        document.getElementById(i).disabled = false;
    }
}