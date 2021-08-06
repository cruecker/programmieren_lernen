#Main - Das ist ein kleines Beispiel Programm
#funktion definieren immer mit eigenen Variablen in einern funktion arbeiten
def rechnen(gr):
    gewicht=input('Gewicht: ')
    if not gewicht:
        return
    return round(float(gewicht)/(float(gr)**2),2)

def auswerten(b):
    if b>=25:
        print('Übergewicht')
    elif b<18.5:
        print('Untergewicht')
    else:
        print('Normalgewicht')

def hinzufuegen(n,b):
    #prüfen ob der Name vorhanden ist und hinzufügen
    if n in datenspeicher:
        bmis=datenspeicher[n]
    else:
        bmis=[]
    bmis.append(b)
    datenspeicher.update({n:bmis})

def ausgeben():
    #ausgabe des Inhalt des Dicts
    for i in datenspeicher.items():
        print(i)

#Name eingeben
name = input("Bitte Ihren Namen eingaben: ")
print("Hallo", name)

#grösse eingeben
groesse=input('Körpergrösse: ')

#dictionary definieren
datenspeicher={}

while True:
    try:
        #Funktion rechnen aufrufen
        bmi=rechnen(groesse)
        if not bmi:
            break
    except ValueError:
        continue

    #Funktion auswerten aufrufen
    auswerten(bmi)
    hinzufuegen(name,bmi)
ausgeben()
