#definieren einer Klasse
class Katze:
    Name = "Nemo"
    Alter = 15
    def lautgeben(self):
        print("Miau!")

#Klasse instanzieren, constructor erstellen, muss immer gemacht werden
obj = Katze()
print(type(obj))

#aufrufen der funktion lautgeben
obj.lautgeben()

#aufrufen der eigenschaft alter
print(obj.Alter)
