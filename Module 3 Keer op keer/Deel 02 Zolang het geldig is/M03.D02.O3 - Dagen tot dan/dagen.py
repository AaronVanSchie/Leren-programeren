week = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
dag = input("Geef een dag van de week op: ")

while dag != week[0]:
    print(week[0])
    week.pop(0)