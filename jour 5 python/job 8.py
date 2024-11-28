def somme_valeurs_paires(liste):
    # Initialiser la somme à zéro
    somme = 0
    # Parcourir chaque élément de la liste
    for element in liste:
        # Ajouter à la somme si l'élément est pair
        if element % 2 == 0:
            somme += element
    return somme

# Exemple d'utilisation
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
resultat = somme_valeurs_paires(L)
print("La somme des valeurs paires dans la liste est:", resultat)
