'''Main - Das ist ein kleines Beispiel Programm'''

class Benutzer:
    def __init__(self):
        self.name = input("Bitte Ihren Namen eingaben: ")
        self.groesse=input('Körpergrösse: ')

class Bmirechner:
    '''funktion definieren immer mit eigenen Variablen in einern funktion arbeiten'''
    def __init__(self):
        self.datenspeicher={}
        
    def rechnen(self,gr):
        gewicht=input('Gewicht: ')
        if not gewicht:
            return
        return round(float(gewicht)/(float(gr)**2),2)

    def auswerten(self,b):
        if b>=25:
            print('Übergewicht')
        elif b<18.5:
            print('Untergewicht')
        else:
            print('Normalgewicht')

    def hinzufuegen(self,n,b):
        '''prüfen ob der Name vorhanden ist und hinzufügen'''
        if n in self.datenspeicher:
            bmis=self.datenspeicher[n]
        else:
            bmis=[]
        bmis.append(b)
        self.datenspeicher.update({n:bmis})

    def ausgeben(self):
        '''ausgabe des Inhalt des Dicts'''
        for i in self.datenspeicher.items():
            print(i)

'''dictionary definieren'''

benutzer=Benutzer()
bmirechner=Bmirechner()

while True:
    try:
        '''Funktion rechnen aufrufen'''
        bmi=bmirechner.rechnen(benutzer.groesse)
        if not bmi:
            break
    except ValueError:
        continue

    '''Funktion auswerten aufrufen'''
    bmirechner.auswerten(bmi)
    bmirechner.hinzufuegen(benutzer.name,bmi)
bmirechner.ausgeben()
