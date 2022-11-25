spielfeld = [
    [2, 4, 8, 8, 32, 2],
    [2, 2, 8, 16, 16, 8],
    [4, 8, 2, 2, 2, 16],
    [2, 4, 8, 16, 2, 4],
    [8, 8, 16, 2, 2, 2],
    [8, 4, 2, 4, 16, 32]
]


def mache_spielfeld():
    zeile = 1
    print('  +', end='')
    print(len(spielfeld[1]) * '-------+')
    for line in spielfeld:
        print(zeile, end='')
        print(' |', end='')
        print(len(spielfeld[1]) * '       |')
        print('  ', end='')
        for field in line:
            if field == 0:
                print(f'|       ', end='')
            elif field > 9:
                print(f'|   {field}  ', end='')
            elif field > 99:
                print(f'|  {field}  ', end='')
            else:
                print(f'|   {field}   ', end='')
        print('|')
        print('  |', end='')
        print(len(spielfeld[1]) * '       |')
        print('  +', end='')
        print(len(spielfeld[1]) * '-------+')
        zeile = zeile + 1


def spaltennummer():
    spalte = 1
    print('  ', end='')
    for field in range(len(spielfeld[0])):
        if field == len(spielfeld[0]) - 1:
            print(spalte)
        else:
            print(spalte, end='       ')
            spalte = spalte + 1


spaltennummer()
mache_spielfeld()


def eingabe():
    koordinaten = input('Gib eine Zeilen- und danach eine Spaltennummer ein:')
    koordinaten_als_liste = koordinaten.split(' ')
    return koordinaten_als_liste


def auswerten(zeile, spalte):
    zeile = int(zeile) - 1
    spalte = int(spalte) - 1
    # im Spielfeld die richtige Liste (zeile), dann richtige Position in Liste (spalte)
    spielfeld[zeile][spalte] = 0


x, y = eingabe()
auswerten(x, y)
mache_spielfeld()
