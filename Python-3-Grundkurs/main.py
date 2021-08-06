#Main - Das ist ein kleines Beispiel Programm

name = input("Bitte Ihren Namen eingaben: ")
print("Hallo", name)

groesse=input('Körpergrösse: ')


bmis=[]
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
    bmis.append(bmi)

for bmi in bmis:
    print(bmi)
