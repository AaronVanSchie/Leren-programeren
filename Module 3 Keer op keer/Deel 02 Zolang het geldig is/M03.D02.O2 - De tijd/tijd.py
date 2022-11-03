tijd = 0

while True:
    print(f"{tijd} AM")
    tijd = tijd + 1
    if tijd > 12:
        break

tijd = tijd - 12

while True:
    print(f"{tijd} PM")
    tijd = tijd + 1
    if tijd > 12:
        break