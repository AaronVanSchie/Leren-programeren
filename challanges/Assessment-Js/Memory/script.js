const images = [
    'images/bacardi.jpg',
    'images/malibu.jpg',
    'images/vodka.jpg',
    'images/passoa.jpg',
    'images/wiskey.jpg',
];

const kaarten = images.concat(images);

let turns = 0;
let flippedkaartjes = [];
let checked = [];
let gameend = false;

const turnDisplay = document.getElementById('turns');
const Board = document.getElementById('images');

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

function flipCard() {
    this.firstChild.classList.remove('hidden');
    this.classList.add('selected');

    if (flippedkaartjes.length === 0) {
        flippedkaartjes.push(this);
    } else if (flippedkaartjes.length === 1) {
        flippedkaartjes.push(this);
        let isMatch = flippedkaartjes[0].firstChild.src === flippedkaartjes[1].firstChild.src;
    
    if (isMatch) {
        flippedkaartjes = [];
    } else {
        setTimeout(() => {
            flippedkaartjes[0].firstChild.classList.add('hidden');
            flippedkaartjes[1].firstChild.classList.add('hidden');
    
            flippedkaartjes[0].classList.remove('selected');
            flippedkaartjes[1].classList.remove('selected');

            flippedkaartjes = [];
        }, 1000);
        turns += 1
        turnDisplay.textContent = turns;
    }
    }
}

createBoard();