# + : addition
# - : soustraction
# * : multiplication
# ** : puissance
# / : division flottante (10 / 3 = 3.33333)
# // : division entière (10 // 3 = 3)
# % : reste d'une division
# ! : inversion de valeur (True devient False, False devient True)

# > : plus grand que
# < : plus petit que
# >= : plus grand ou égale à
# <= : plus petit ou égale à
# == : égal à
# != : différent de

valeur = 5
#print(valeur)

valeur += 10
#print(valeur)

valeur + 10
#print(valeur)


if valeur > 10:
    print("Valeur plus grande que 10")
else:
    print("Valeur plus petite que 10")


while valeur < 100:
    valeur += 1

for i in range(10):
    valeur += 1


#print(valeur)
def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    
#print(max(valeur, 5, 50)) # Affiche 50

def multiplier_pair(nombre, multiplicateur):
    if nombre % 2 == 0:
        return nombre * multiplicateur

    return nombre

#print(multiplier_pair(valeur, 2)) # Affiche 25


def additionner(nombre, valeur, nombre_de_fois):
    for i in range(nombre_de_fois):
        nombre += valeur
    
    return nombre

#print(additionner(valeur, 10, 5)) # Affiche 75


#Faire la fonction est_pair qui prends en paramètre nombre et renvoie True si le nombre est pair
def est_pair(nombre):
    return nombre % 2 == 0


#Faire la fonction clamp qui prends en paramètre min, max, valeur et qui renvoie :
# - Valeur si valeur est entre min et max
# - Min si valeur est plus petite que min
# - Max si valeur est plus grande que max
def clamp(min, max, valeur):
    if valeur < min:
        return min
    if max < valeur:
        return max
    
    return valeur



#Faire une fonction afficher_nombres qui prends en paramètre une valeur et qui affiche tous les nombres jusqu'à la valeur
def afficher_nombres(valeur):
    for nombre in range(valeur):
        print(nombre)

afficher_nombres(10)


#Faire une fonction afficher_paires qui prends en paramètre une valeur et qui affiche tous les nombres paires inférieurs à la valeur
def afficher_pairs(valeur):
    for nombre in range(0,valeur,2):
        print(nombre)



# Faire une fonction compter_multiples qui prends en paramètre une valeur et un multiplicateur et qui renvoie la quantité de nombres multiples de multiplicateur entre 0 et valeur
# Créer d'abord une variable compteur qui vaut 0
# Répéter l'action "Si nombre est multiple de multiplicateur, ajouter 1 à compteur" pour chaque nombre entre 0 et valeur
# Renvoyer compteur
def compter_multiples(valeur, multiplicateur):
    compteur = 0
    for nombre in range(valeur):
        if nombre % multiplicateur == 0:
            compteur += 1
            
    return compteur