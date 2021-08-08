'''Module BMI'''
'''Main - Das ist ein kleines Beispiel Module für den BMI'''
import sqlite3
import os.path

class Benutzer:
    def __init__(self):
        self.name = input("Bitte Ihren Namen eingaben: ")
        self.groesse=input('Körpergrösse: ')

class Bmirechner:
    '''funktion definieren immer mit eigenen Variablen in einern funktion arbeiten'''
    def __init__(self):
        self.datenspeicher={}
        if not os.path.exists('bmi.db'):
            connection=sqlite3.connect('bmi.db')
            cursor=connection.cursor()
            '''real = flaot in SQL'''
            cursor.execute('''CREATE TABLE bmirechner(name TEXT,bmi REAL)''')
        else:
            connection=sqlite3.connect('bmi.db')
            cursor=connection.cursor()
            cursor.execute('''SELECT name,bmi FROM bmirechner ''')
            rows=cursor.fetchall()
            for row in rows:
                name=row[0]
                bmi=row[1]
                if name in self.datenspeicher:
                    bmis=self.datenspeicher[name]
                else:
                    bmis=[]
                bmis.append(bmi)
                self.datenspeicher.update({name:bmis})
            
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
        connection=sqlite3.connect('bmi.db')
        cursor=connection.cursor()
        '''real = flaot in SQL'''
        cursor.execute('''INSERT INTO bmirechner VALUES(?,?) ''',(n,b))
        connection.commit()
        connection.close()

    def ausgeben(self):
        '''ausgabe des Inhalt des Dicts'''
        for i in self.datenspeicher.items():
            print(i)
