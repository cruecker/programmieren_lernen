person = ["Hans", "Otto"]
print(person[0])
person2 = {"Vorname": "Otto", "Nachname": "Hans"}
print(person2["Vorname"])

for v in person2:
    print(v)
for v in person2.values():
    print(v)
for v in person2.keys():
    print(v)

person2.update({"Vorname": "Willie"})
for v in person2.values():
    print(v)
