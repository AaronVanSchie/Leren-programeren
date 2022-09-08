print("Een getal onder de 100?")
a = int(input())
print("Een getal onder de 100?")
b = int(input())
if a > b:
    max = a
    min = b
    print("de maximum is a\nde minimum is b")
elif a < b:
    max = b
    min = a
    print("de maximum is b\nde minimum is a")
else :
    print("a is gelijk aan b")