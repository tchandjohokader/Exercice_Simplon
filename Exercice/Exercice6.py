def modifier_liste(liste, nbr, replacement):
    for i in range(len(liste)):
        if liste[i] == nbr:
            liste[i] = replacement
        elif isinstance(liste[i], list):
            modifier_liste(liste[i], nbr, replacement)

liste1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]

modifier_liste(liste1, 58, 5800)

print(liste1)
