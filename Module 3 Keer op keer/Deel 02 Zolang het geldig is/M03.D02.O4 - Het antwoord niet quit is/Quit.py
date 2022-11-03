aantal = 1
vraag = input(f"? ").lower()

while vraag != "quit":
    vraag = input(f"? ({aantal}) ")
    aantal += 1