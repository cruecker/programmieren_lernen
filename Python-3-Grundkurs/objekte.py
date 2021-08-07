class Benutzer:
    name=''
    groesse=0.0
    #Methode definieren
    def anmelden(self):
        print("Anmeldung: ", self.name)
    #Magic Methode
    #initialisieren
    def __init__(self,name,groesse):
        self.name=name
        self.groesse=groesse
    #StingAusgabe statt 0x...
    def __str__(self):
        return 'Benutzer: ' + self.name
    #distructor Methode
    def __del__(self):
        print('Ich werde gelöscht!')

class Administrator(Benutzer):
    def __init__(self,name,groesse,kennwort):
        self.name=name
        self.groesse=0.0
        self.kennwort=kennwort
    #Methode definieren
    #StingAusgabe statt 0x...
    def __str__(self):
        return 'Benutzer: ' + self.name + ' hat das Kennwort: ' + self.kennwort

    

#erstelle objekt der Klasse benutzer mit dem Bauplan der Klasse
benutzer1=Benutzer('Claudius',1.86)
benutzer1.anmelden()
print (benutzer1)

benutzer2=Administrator('Nemo',0.60,'Maus#666')
benutzer2.anmelden()
print (benutzer2)
del benutzer2
#del benutzer1 #zum auslösen der Magic Methode __del__
