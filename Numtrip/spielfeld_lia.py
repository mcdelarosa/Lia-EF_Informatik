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
            if field > 9:
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