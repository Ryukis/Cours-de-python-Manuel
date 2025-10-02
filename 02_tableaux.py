mon_tableau = [15, 1, 2, 3, 4, 5]


print(mon_tableau[0]) # Lire dans le tableau "à la position 0"
mon_tableau[0] += 10 # 15 + 10, on stockera maintenant 25 à la position 0


for valeur in mon_tableau: # parcourir le tableau
    if valeur % 2 == 0:
        print(valeur)

for index, valeur in enumerate(mon_tableau): # énumère le tableau
    if valeur % 2 == 0:
        mon_tableau[index] += 2


mon_tableau.append(10) #On ajoute la valeur 10 à la fin du tableau
mon_tableau.insert(0, 10) #On ajoute la valeur 10 à la position 0
mon_tableau.remove(15) #On retire 15 du tableau
mon_tableau.pop(0) #On retire ce qui se trouve à la position 0
mon_tableau.clear() #Vider le tableau
mon_tableau.reverse() #inverse les valeurs du tableau
mon_tableau.sort() #trier les valeurs du tableau
mon_tableau.index(3) #permet de connaitre la position d'une valeur dans le tableau

# Faire une fonction creer_tableau_paires qui prends en paramètre un nombre
#- Créer une variable mon_tableau qui stocke un tableau vide
#- Faire une boucle for pour chaque valeur de 0 à nombre
#- Si valeur est pair, ajouter valeur au tableau
#- Après la boucle, retourner le tableau
def creer_tableau_paires(nombre):
    mon_tableau = []
    for valeur in range(0 , nombre):
        if valeur % 2 == 0:
            mon_tableau.append(valeur)

    return mon_tableau

# Faire une fonction somme qui prends en paramètre un tableau
# - Commencer par faire une variable compteur qui vaut 0
# - Faire une boucle for pour chaque valeur du tableau
# - Additionner valeur au compteur
# - Après la boucle, renvoyer le compteur
def somme(mon_tableau):
    compteur = 0
    for valeur in mon_tableau:
        compteur += valeur 
    return compteur


# Faire une fonction valeur_max qui prends en paramètre un tableau
# - Commencer par faire une variable v_max qui vaut -1
# - Faire une boucle for pour chaque valeur du tableau
# - Si v_max est plus petite que valeur, dire que v_max vaut valeur
# - Après la boucle, retourner v_max
def valeur_max(mon_tableau):
    v_max = -1
    for valeur in mon_tableau:
        if v_max < valeur:
            v_max = valeur

    return v_max


# Faire une fonction somme_paires qui prends en paramètre un tableau et qui additionne tous les nombres paires du tableau
def somme_paires(mon_tableau):
    compteur = 0
    for nombre in mon_tableau :
        if nombre % 2 :
            compteur += nombre
    
    return compteur
        