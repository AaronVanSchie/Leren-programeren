const cards = ["Cola", "Sprite", "Fanta", "Dr Pepper", "7uP", "Red Bull", "Wiskey", "AA", "Casis", "Water"];
    let flippedCards = [];

    function createCard(card) {
        const element = document.createElement('div');
        element.textContent = card;
        element.classList.add('card');
        element.addEventListener('click',  flipCard(element));
        return element;
    }

    function flipCard(card) {
    }
