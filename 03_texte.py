mon_super_texte = 'Bonjour'

for lettre in mon_super_texte:
    if lettre == 'B':
        print("J'ai trouvé la lettre B")


mon_super_texte[2] == 'n'

majuscule = mon_super_texte.upper()
minuscule = mon_super_texte.lower()
contient_B = mon_super_texte.count("B") > 0
est_un_nombre = mon_super_texte.isdigit()

def est_palindrome(text):
    taille_texte = len(text)
    for i in range(0, taille_texte // 2):
        if text[i] != text[taille_texte - i - 1]:
            return False
        
    return True


# Faire une fonction nombre_de_lettre_est_pair qui prends en paramètre une variable texte qui renvoie True si le nombre de lettre du texte est pair, sinon False
def nombre_de_letttre_est_pair(texte):
    if len(texte) % 2:
        return True
    
    return False


# Faire une fonction est_minuscule qui prends en paramètre un texte qui vérifie si le texte est en minuscule en faisant une boucle
# si le texte contient au moins une lettre en majuscule, renvoyer False
# sinon True
def est_minuscule(texte):
    for lettre in texte:
        if lettre.upper() == lettre:
            return False
        
    return True
