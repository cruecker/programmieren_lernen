#pattern suchen
pattern = "@"
seq1 = "c.ruecker@itcr.de"
print(pattern in seq1)
print(pattern not in seq1)
seq2 = "c.ruecker@itcr.de"
print("seq1 = seq2", seq1 is seq2)
print("seq1 = seq2", seq1 == seq2)
z1 = [2, 3, 5]
z2 = [2, 3, 5]
print("z1 = z2", z1 is z2)
print("z1 = z2", z1 == z2)


z1 = 2
a = z1 << 1
b = z1 >> 1
print("der wert von 2 << 1:" , a)
print("der wert von 2 >> 1:" , b)
