#Tuple nicht änderbar mit runden klammern
print("Tuple")
primzahlen = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
print(primzahlen)

#Listen änderbar mir eckigen Klammern
print("Liste")
primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(primzahlen)
primzahlen.append(39)
print(primzahlen)
primzahlen.pop(len(primzahlen)-1)
print(primzahlen)
