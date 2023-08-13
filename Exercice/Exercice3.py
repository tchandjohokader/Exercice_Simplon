with open("note.txt", "r") as file:
    contenu = file.read()  
contenu_sans_espace = contenu.replace("\n", " ")
print(contenu_sans_espace)
