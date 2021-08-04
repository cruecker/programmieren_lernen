def rechnen(a, b = 8): #b ist optional
    print(a * b)


def multiplizieren(a, *b): #b ist eine liste
    erg = a
    for i in b:
        erg *=i
        print(erg)

rechnen(2)
rechnen(3, 4)

multiplizieren(3)
multiplizieren(3, 5)
multiplizieren(3, 5, 7, 11)
