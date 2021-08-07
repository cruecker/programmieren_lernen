import bmi

'''dictionary definieren'''

benutzer=bmi.Benutzer()
bmirechner=bmi.Bmirechner()

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
