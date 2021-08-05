#definieren einer Klasse
class Person:
    #privat somit nicht sichbar, schütz z.B. vor änderungen
    __alter = 42
    #getter definieren
    def getAlter(self):
        return self.__alter

obj = Person()
print(obj.getAlter())
