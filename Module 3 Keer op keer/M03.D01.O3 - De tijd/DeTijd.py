from time import sleep


for tijd in range(1,13):
    if tijd <= 12:
        print(f"{tijd} AM")
        sleep(0.3)
for tijd in range(1,13):
    if tijd <= 11:
        print(f"{tijd} PM")
        sleep(0.3)
    else:
        print(f"{tijd} PM")
        print("Its midnight")
