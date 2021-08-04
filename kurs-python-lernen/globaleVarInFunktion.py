a = 42
def ausgabe() :
    global a
    a += 1
    print(a)

ausgabe()
print(a)
