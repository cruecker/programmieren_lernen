#definieren einer Klasse
class Tier:
    def __init__ (self, name, alter, typ):
        self.name = name
        self.alter = alter
        self.typ = typ

    def lautgeben(self, text):
        print(text)

#Klasse instanzieren, constructor erstellen, muss immer gemacht werden
obj = Tier("Nemo", 15, "Katze")
print(type(obj))

#aufrufen der funktion lautgeben
obj.lautgeben("Miau!")

#aufrufen der eigenschaft alter
print(obj.alter)

