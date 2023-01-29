from fruitmand import fruitmand
import random

user_input = int(input("Hoeveel: "))

for i in range(user_input):
    random_fruit = random.randint(0, len(fruitmand))
    print(fruitmand[random_fruit]['name'])