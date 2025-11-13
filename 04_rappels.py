# Faire une fonction max qui prend en paramètre un tableau de nombres et qui renvoie la plus grande valeur du tableau
def max(tableau):
    nombre = tableau[0]
    for mz in tableau:
        if mz > nombre:
            nombre = mz
    return nombre



# Faire une fonction compter_lettre qui prends en paramètre un texte et une lettre, renvoyer le nombre de fois que la lettre se trouve dans le texte
# /!\ Attention, le code doit pouvoir détecter la lettre qu'elle soit en minuscule ou en majuscule

def compter_lettre(texte,lettre):
    texte = texte.lower()
    lettre = lettre.lower()
    compter = 0
    for dgz in texte:
        if dgz == lettre:
            compteur += 1
         
    return compteur

# Faire une fonction afficher_paires qui prends en paramètre un début et une fin.
# Afficher (print) toutes les valeurs qui se trouvent entre début et fin.
def afficher_paires (debut,fin):
    for i in range (debut,fin):
        if i % 2 == 0 :
            print (i)



#Faire une fonction afficher_texte qui prends en paramètre un texte et qui affiche le texte (avec un print)
def afficher_texte(texte):
    print(texte)


# Faire une fonction afficher_nombre_lettres qui prends en paramètre un texte et 
# qui affiche le nombre de lettres qui se trouvent dans le texte
def afficher_nombre_lettres(texte):
    print (len(texte))



# Faire une fonction compter_type_lettre qui prends en paramètre un texte
# Compter le nombre de minuscules puis l'afficher
# Compter le nombre de majuscules puis l'afficher
# Compter le nombre de voyelles puis l'afficher
# Compter le nombre d'espaces puis l'afficher
def compter_type_lettre(texte):
    majuscul = 0
    minuscul = 0
    for lettre in texte :
        if lettre == lettre.lower():
            minuscul += 1
        if lettre == lettre.upper():
            majuscul += 1
        
    print("Nombre de minuscules : " + minuscul + " lettres")
    print("Nombre de majuscules : " + majuscul + " lettres")