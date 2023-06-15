const plaatjes = [
    'images/bacardi.jpg',
    'images/malibu.jpg',
    'images/vodka.jpg',
    'images/passoa.jpg',
    'images/wiskey.jpg',
];

var nummer = 0
const afbeelding = document.getElementById("Afbeelding");
const vorige = document.getElementById("Vorige");
const volgende = document.getElementById("Volgende");

function Update(nummer) {
    afbeelding.src = plaatjes[nummer];
  }
    vorige.addEventListener("click", () => {
        if (nummer === plaatjes.length) {
            nummer = 0;
        }  if (nummer == 0) {
            nummer = plaatjes.length -1
        } else {
            nummer -= 1;
        }
            Update(nummer);
    });

    volgende.addEventListener("click", () => {
        if (nummer === plaatjes.length) {
            nummer = 0;
        } if (nummer == plaatjes.length - 1) {
            nummer = 0
        } else {
            nummer += 1;
        }
            Update(nummer);
    });

Update(nummer);