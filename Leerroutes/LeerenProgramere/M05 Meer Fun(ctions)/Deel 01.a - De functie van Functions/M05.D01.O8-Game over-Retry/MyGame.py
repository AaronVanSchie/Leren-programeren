from random import randint
from time import sleep

andwoord1 = ""
andwoord2 = ""

def quests(vraag):
    while True:
        andwoord1 = input(vraag).lower()
        if andwoord1 == "ja" or andwoord1 == "yes":
            print()
            andwoord1 = False
            break
        elif andwoord1 == "nee" or andwoord1 == "no":
            print(randomdeath)
            andwoord1 = True
            break
        else:
            print()
    return andwoord1


def leftorright(vraag):
    while True:
        andwoord2 = input(vraag).lower()
        if andwoord2 == "left" or andwoord2 == "links":
            print()
            andwoord2 = False
            break
        elif andwoord2 == "rechts" or andwoord2 == "right":
            print()
            andwoord2 = True
            break
        else:
            print()
    return andwoord2


repeat = True
punten = 0

while repeat == True:
    randomdeath = randint(1, 3)
    if randomdeath == 1:
        randomdeath = "Narrator: The towns folks burned you in a fire."
    elif randomdeath == 2:
        randomdeath = "Narrator: The towns murderer killed you in your sleep."
    else:
        randomdeath = "Narrator: You had a heart attack."

    randomweapon = randint(1, 4)
    if randomweapon == 1:
        randomweapondict = {
          "Type": "Slipper",
          "Damage": 1000,
        }
    elif randomweapon == 2:
        randomweapondict = {
          "Type": "Sword",
          "Damage": 4,
        }
    elif randomweapon == 3:
        randomweapondict = {
          "Type": "Katana",
          "Damage": 10,
        }
    else:
        randomweapondict = {
          "Type": "Knife",
          "Damage": 2,
        }

    input(f'''
| Pres enter to start  ''')
    print()
    input("Narrator: Hello there!")
    input("Narrator: i am the games Narrator.")
    name = input("Narrator: And what may be your name? : ")
    input("Narrator: Troughout the game you can collect points by awnsering correctly or attacking in the final boss fight")
    print()
    input("Loading Game....")
    print()
    input("Unknown Character: O your finally awake. ")
    input("Farmer Hendrickson: My name is Hendrick i am the towns farmer.")
    input(f"Farmer Hendrickson: You must be {name}!")
    input("Farmer Hendrickson: I have heard alot of stories about you.")
    input("Farmer Hendrickson: Would you like to do something for me? ")
    print()

    quest1 = quests("Narrotor: Would you like to accept the Farmer Hendrick his quest? ").lower()
    if andwoord1:
        break
    else:
        punten += 1

    input("Farmer Hendrickson: I will lead you on your way tommorow you should first get some rest.")
    print()
    input("Narrator: The Next Day.")
    print()
    input(f"Farmer Hendrickson: Goodmorning {name}!")
    input("Farmer Hendrickson: Your quest from me is as followed.")
    input("Farmer Hendrickson: You need to go look for 10 hay bales in the forest.")
    input("Farmer Hendrickson: Thanks again.")
    input("Farmer Hendrickson: Good luck on your Journey.")
    print("")
    input("Narrator: After walking for 2 hours your road seems to split two ways.")

    leftorright1 = leftorright("Narrator: Do you want to take the left or right path? ").lower()
    if andwoord2:
        input("Narrator: You havent found the hay bales.")
        input("Narrator: You starved to death.")
        break
    else:
        punten += 1

    input("Narrator: After walking for a couple of hours u see something in the distance.")
    input("Narrator: It looks like the hay bales Farmer Hendrick looked for.")
    input("Narrator: After collecting the hay bales u return to Farmer Hendrick.")
    print()
    input("Farmer Hendrickson: Thank you so mutch!")
    input("Farmer Hendrickson: I really appreciate your help.")
    input("Farmer Hendrickson: There is one more thing though.")
    input("Farmer Hendrickson: Would you like to do one more thing for me?")
    print()

    quest2 = quests("Narrator: Would you like to accept the Farmer Hendrick his quest? ")
    if andwoord1:
        input("Hendrick killed u")
        break
    else:
        punten += 1

    input("Farmer Hendrickson: Thank you!")
    input("Farmer Hendrickson: My only daughter has been missing for a couple of days now.")
    input("Farmer Hendrickson: The last thing she went to do is, visit her friend at the kings castle.")
    print()
    input("Narrator: You have been walking pretty long time now and stil havent seen the castle.")
    input("Narrator: After a few more miles the road splits up and you have to make a discision.")

    leftorright2 = leftorright("Narrator Wich way do you want to go Left or Right?")
    if andwoord2:
        input("Narrator: You sadly went the wrong way and never found his daughter or any food source.")
        input("Narrator: You starved to death.")
        break
    else:
        punten += 1

    input("Narrator: You took the Left path wich led you to the castle.")
    input("Narrator: When entering the castle you heared a girly scream comming from one of the rooms")
    input("Narrator: You went to see what was going on and you saw ....")
    input("Narrator: You couldnt believe what you saw.")
    input("Narrator: It was Farmer Hendrickson his daughter stuck in the dungeon.")
    input("Narrator: After trying to get her free from the dungeon but you heard someone walk towards you.")
    input("Narrator: It looks to be the King, he dident look really pleased with you arrival.")
    print()
    input("King Arthur: What do you think your doing!")
    option = input("Narrator: Do you awnser? ")
    if option == "yes" or option == "ja":
        print()
        input(f"{name}: Im here to save Farmer Hendrickson his daughter!")
        print()
        input("King Arthur: I Wont alouw you to do that.")
        input("King Arthur: You cant take away my slave!")
        input("King Arthur: You know what i have a bether idea!")
        input("King Arthur: Why dont you fight my best soldier.")
        input("King Arthur: If you win you can take her back to her father.")
        input("King Arthur: But if you lose she wil stay with me.")
        input("King Arthur: And you will be executed.")
        print()
    elif option == "no" or option == "nee":
        input("Narrator: The king fel to the ground and died of cancer")
        break
    else:
        input("Narrator: You died of ligma")
        break
    quest3 = input("Narrator: Do you accept King Arthur his offer?")
    if andwoord1:
        input("King Arthur: Are you scared or something?")
        input("King Arthur: I geus this is the last thing anyone wil remember about you")
        input(f"King Arthur: Was nice knowing you {name}.")
        input("Narrator: King Arthur shot you with his crossbow.")
        break
    else:
        punten += 1
        print()
    input("Narrator: The fight begins here is you weapon.")
    print(f"You aquired", randomweapondict["Type"])
    print()
    input("Soldier Ala: Are you ready to die!")
    print()
    input("Narrator: I forgot to tell you but here is some information about Soldier Ala.")
    input("Narrator: He has 100 Hp and does 100 Damage.")
    input("Narrator: You have 1000 Hp.")
    print()
    input("Soldier Ala: Lets get this started!")
    print()

    soldierhp = 60
    soldierdmg = 100
    playerHp = 1000

    while playerHp > 0:
        input("Narrator: Soldier Ala delt 100 Damage")
        input(f"Narrator: Your hp has dropped to {playerHp - soldierdmg}.")
        print("Narrator: You hit Soldier Ala for.", randomweapondict["Damage"])
        sleep(1)
        print("Narrator: Soldier Ala his hp has dropped to.", soldierhp - randomweapondict["Damage"])
        if playerHp - soldierdmg <= 0:
            print()
            print("Narrator: You have lost the battle and have sadly died.")
            print()
            input("Narrator: King Arthur shot you died with his crossbow")
            print(f'''
| Dear {name}
| You have sadly died in the fight and dident complete Farmer Hendrickson`s quest
| You may rest in piece now

    YOU DIED!!
            ''')
            break
        elif soldierhp - randomweapondict["Damage"] <= 0:
            print()
            print("Narrator: You have won the battle!")
            print()
            break
        else:
            print()
            punten += 1
        soldiermdg = soldierdmg + 100
        playerHp = playerHp - soldierdmg
        soldierhp = soldierhp - randomweapondict["Damage"]

    if playerHp - soldierdmg <= 0:
        break

    input("Narrator: After winning your fight against Soldier Ala you walk towards King Arthur")
    print()
    input(f"{name}: Give me Farmer Hendricksons daughter i have won your battle!!")
    input("King Arthur: FINE!!")
    input("King Arthur: Here you go")
    print()
    input("Narrator: You go back to Farmer Hendrickson")
    print()
    input(f"Farmer Hendrickson: THANK YOU SO MUCH {name} i dont know how to thank you for this.")
    input("Farmer Hendrickson: Im speachless")
    print()
    input("Narrator: Farmer Hendrickson invited everyone for a party to thank you for bringing his daughter back!")
    input("Narrator: You partied the whole night and day.")
    input("Narrator: And Nothing bad ever happend again!")
    print(f'''
| Dear {name}
| Everyone from the town would like to thank you for your help and support
| You may go back to your own town now!

    YOU WON!!
    ''')
    break

again = input("Would u like to play again? J/N ").upper()
if again == "J":
    repeat = True
else:
    repeat = False
    print(f"Your final score is {punten}")
    quit()
