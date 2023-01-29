def getallenreeks(i):
    i -= 2
    reeks = [0,1]
    for fib in range(i):
        reeks.append(reeks[-1] + reeks[-2])
    return reeks

getallenreeks(int(input("hoeveel?")))
