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
        if (!card.classList.contains('flipped')) {
            card.classList.add('flipped');
            flippedCards.push(card);

            if (flippedCards.length === 2) {
                setTimeout(() => {
                    const [card1, card2] = flippedCards;
                    if (card1.textContent === card2.textContent) {
                        flippedCards = [];
                    } else {
                        card1.classList.remove('flipped');
                        card2.classList.remove('flipped');
                        flippedCards = [];
                    }
                }, 1000);
            }
        }
    }