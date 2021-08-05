#definieren einer Klasse
class Lebewesen:
    alter = 42

class Mensch(Lebewesen):
    name = "Hans"

obj = Mensch()
print(obj.alter, obj.name)
