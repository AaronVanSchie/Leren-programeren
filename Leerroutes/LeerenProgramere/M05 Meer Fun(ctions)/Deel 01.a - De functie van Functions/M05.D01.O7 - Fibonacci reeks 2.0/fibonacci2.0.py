def fibo(nummer: int):
    reeks = [0, 1]

    def fiboReeks(limiet: int):
        if len(reeks) == limiet:
            return

        reeks.append(reeks[-2] + reeks[-1])
        fiboReeks(limiet)

    fiboReeks(100)

    if nummer in reeks:
        print(reeks[0:reeks.index(nummer)+ 1])

fibo(34)