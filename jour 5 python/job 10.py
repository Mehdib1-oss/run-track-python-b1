def produit_intervalle(liste, debut, fin):
    produit = 1  
    for element in liste:
        
        if debut <= element <= fin:
            produit *= element 
    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit_resultat = produit_intervalle(L, 25, 90)
print("Le produit des valeurs dans l'intervalle [25, 90] est:", produit_resultat)
