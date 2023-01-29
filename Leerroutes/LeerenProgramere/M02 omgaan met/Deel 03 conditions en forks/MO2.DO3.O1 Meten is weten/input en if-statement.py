print("Een getal onder de 100?")
a = int(input())
print("Een getal onder de 100?")
b = int(input())
if a > b:
    max = a
    min = b
elif a < b:
    max = b
    min = a

if a != b:
    print("Het maximum is: " , max)
    print("Het minimum is: " , min)
else:
    print("a en b zijn gelijk!")