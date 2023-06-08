const images = [
    'images/bacardi.jpg',
    'images/malibu.jpg',
    'images/vodka.jpg',
    'images/passoa.jpg',
    'images/wiskey.jpg',
];

const kaarten = images.concat(images);

let score = 0;
let flippedkaartjes = [];

const scoreDisplay = document.getElementById('score');
const kaartjes = document.getElementById('images');

function shuffle(kaartje) {
    let IndexNu = kaartje.length;
    let Value, randomIndex;

    while (IndexNu !== 0) {
        randomIndex = Math.floor(Math.random() * IndexNu);
        IndexNu -= 1;
        Value = kaartje[IndexNu];
        kaartje[IndexNu] = kaartje[randomIndex];
        kaartje[randomIndex] = Value;
    }

    return kaartje;
}

function createBoard() {
    const shuffeld = shuffle(kaarten);
    for (let i = 0; i < shuffeld.length; i++) {
        const card = document.createElement('div');
        card.classList.add('card');
        card.dataset.cardIndex = i;

        const kaart = document.createElement('img');
        kaart.src = shuffeld[i];
        kaart.classList.add('hidden');

        card.appendChild(kaart);
        Board.appendChild(card);

        card.addEventListener('click', flipCard);
    }
}