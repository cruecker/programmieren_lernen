#i Name des Zählers wenn i verwendet j nehmen dann k
#Schleifenzähler immer nur um 1 erhöhen
i = 0
while (True):
    i+= 1
    print("Wert des Schleifenzählers",  i)
    if i > 5:
        break #sprunganweisung
print("Schleife beendet")
    
i = 0
while (i < 10):
    i+= 1
    if ((i % 2) != 0):
        continue #sprunganweisung
    print("Wert des Schleifenzählers",  i)
print("Schleife beendet")
