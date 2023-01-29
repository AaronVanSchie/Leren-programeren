tijd = 1

while True:
    print(f"{tijd} AM")
    tijd = tijd + 1
    if tijd > 12:
        break

tijd -= 12

while True:
    print(f"{tijd} PM")
    tijd = tijd + 1
    if tijd > 12:
        break