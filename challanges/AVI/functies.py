EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
END_OF_SENTENCE = ".!?"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    count_char = 0
    for character in text:
        if character in ALLOWED_IN_WORD:
            count_char += 1
    return count_char

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    count_sen = 0
    for character in text:
        if character in END_OF_SENTENCE:
            count_sen += 1
    return count_sen

# opdracht 3
def getNumberOfWords(text: str) -> int:
    text.strip()
    return len(text.split(" "))

# opdracht 4
def getAviScore(text: str) -> int:
    word = getNumberOfWords(text)
    sen = getNumberOfSentences(text)
    Avarage = word / sen

    if Avarage <= 7:
        Avi = 5
    elif 8 >= Avarage > 7:
        Avi = 6
    elif 9 >= Avarage  > 8:
        Avi = 7
    elif 10 >= Avarage > 9:
        Avi = 8
    elif 11 >= Avarage > 10:
        Avi = 11
    elif Avarage > 11:
        Avi = 12

    return int(Avi)