#Tupel nicht veränderbar
gewichte1 = (76, 76.5)
gewichte2 = (65, 64.5)
gewichte = (gewichte1,gewichte2)
print(gewichte)

#Liste veränderbar
gewichte1 = [76, 76.5]
gewichte2 = [65, 64.5]
gewichte = [gewichte1,gewichte2]
print(gewichte)

#aufrufen eines Wertes aus dem Tupel oder der Liste
a = gewichte[1]
print(a)

gruss = "Hallo Welt"
print(gruss[2])
print(gruss[1:4])

#Zusammensetzten
z = "Hallo " + "Welt"
print(z)

#Liste Zusammensetzen
gewichte = [gewichte1+gewichte2]
print(gewichte)

gewichte3 = 2*gewichte
print(gewichte3)

#hinzufühen und löschen aus Liste
gewichte = [76, 76.5, 88]
print(gewichte)
del gewichte[1]
print(gewichte)
gewichte.insert(0,99)
print(gewichte)
#entfernen der Zahl ohne den Index zu verwenden
gewichte.remove(76)
print(gewichte)
gewichte.append(95)
print(gewichte)

#String aendern
print(gruss)
gruss_neu = gruss.replace("l","n")
print(gruss_neu)
gruss = gruss.replace("l","n")
print(gruss)
