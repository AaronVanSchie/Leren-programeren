function changeImage(getal){
    const container = document.getElementById("container");
    container.style.backgroundImage = "url(images/bg"+getal+".jpg)";
    const picture = document.getElementById("picture");
    picture.src = "images/"+getal+".jpg";
    document.getElementById(getal).innerHTML = Number(document.getElementById(getal).innerHTML) + 1;
}