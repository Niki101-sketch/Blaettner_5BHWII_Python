import random


def _arrayFuellenPlusZiehen():
    zahlen = list(range(1, 46))

    gezogen = 1
    count = 0
    while True:
        if gezogen <= 6:
            index = random.randrange(len(zahlen) - count)
            iZahl = zahlen.pop(index)
            print(iZahl)
            zahlen.append(iZahl)
            count = count + 1
            gezogen = gezogen + 1
        else:
            break

    return zahlen[-6:]


def lottoStatistik(anzahlZiehungen):
    statistik = {}
    for zahl in range(1, 46):
        statistik[zahl] = 0

    for i in range(anzahlZiehungen):
        for zahl in _arrayFuellenPlusZiehen():
            statistik[zahl] = statistik[zahl] + 1

    for zahl, anzahl in statistik.items():
        print(zahl, ":", anzahl)


lottoStatistik(1000)