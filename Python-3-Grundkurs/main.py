#Main - Das ist ein kleines Beispiel Programm

name = input("Bitte Ihren Namen eingaben: ")
print("Hallo", name)

groesse=input('Körpergrösse: ')


datenspeicher={}
while True:
    gewicht=input('Gewicht: ')
    if not gewicht:
        break
    try:
        bmi=round(float(gewicht)/(float(groesse)**2),2)
    except ValueError:
        continue
    print('BMI: ', bmi)
    if bmi>=25:
        print('Übergewicht')
    elif bmi<18.5:
        print('Untergewicht')
    else:
        print('Normalgewicht')
    #prüfen ob der Name vorhanden ist und hinzufügen
    if name in datenspeicher:
        bmis=datenspeicher[name]
    else:
        bmis=[]
    bmis.append(bmi)
    datenspeicher.update({name:bmis})
#ausgabe des Inhalt des Dicts
for i in datenspeicher.items():
    print(i)
