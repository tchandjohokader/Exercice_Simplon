mot = "foutou"
resultat = ""

for i in range(len(mot)):
    if i % 2 == 0:
        resultat += mot[i].upper()
    else:
        resultat += mot[i].lower()

print(resultat)
