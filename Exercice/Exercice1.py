def reverse_list(input_list):
    liste_renver = input_list[::-1]
    return liste_renver

liste_original = [1, 2, 3, 4, 5]

liste_final = reverse_list(liste_original)

print("Liste originale:", liste_original)
print("Liste inversée:", liste_final)
