from audioop import mul
from time import sleep

multiply = int(input('Welk getal moet je vermenigvuldigen? '))

nummer = 0

for i in range(1, 11): 
    print(f" { i + nummer} x {multiply} = {i * multiply}")
    sleep(0.3)
