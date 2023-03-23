var image = document.getElementById("image");

document.onkeydown = checkKey;
image.style.transform = "rotate(90deg)"

totaal = 0
posLeft = 50
posTop = 50


var rij = 5

function move(direction){
    if (direction == "Up"){
        image.style.backgroundPosition = `${totaal}px 0px`;
        image.style.top = `${posTop}px`;
        image.style.transform = "rotate(0deg)"
        totaal = totaal - 84
        posTop = posTop - rij
    } else if(direction == "Down"){
        image.style.backgroundPosition = `${totaal}px 0px`;
        image.style.top = `${posTop}px`;
        image.style.transform = "rotate(180deg)"
        totaal = totaal + 84
        posTop = posTop + rij
    } else if (direction == "Left"){
        image.style.backgroundPosition = `${totaal}px 0px`;
        image.style.left = `${posLeft}px`;
        image.style.transform = "rotate(270deg)"
        totaal = totaal - 84
        posLeft = posLeft - rij
    } else if (direction == "Right"){
        image.style.backgroundPosition = `${totaal}px 0px`;
        image.style.left = `${posLeft}px`;
        image.style.transform = "rotate(90deg)"
        totaal = totaal + 84
        posLeft = posLeft + rij
    }
}

function checkKey(e) {
	console.log("key nr = " + e.keyCode);
    e = e || window.event;
    if (e.keyCode == 32){
    	console.log("spacebar");
    } else if (e.keyCode == '38') {
        move("Up")
        console.log("Up arrow");
    } else if (e.keyCode == '40') {
        move("Down")
        console.log("down arrow");
    } else if (e.keyCode == '37') {
        move("Left")
    	console.log("left arrow");
    } else if (e.keyCode == '39') {
        move("Right")
    	console.log("right arrow"); 
    }
}