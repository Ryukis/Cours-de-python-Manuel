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