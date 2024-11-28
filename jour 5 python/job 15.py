def arrondir_et_trier(liste):
    liste_arrondie = []
    
    for nombre in liste:
        if nombre - int(nombre) >= 0.5:
            nombre_arrondi = int(nombre) + 1
        else:
            nombre_arrondi = int(nombre)
        
       
        liste_arrondie.append(nombre_arrondi)

    
    for i in range(len(liste_arrondie) - 1): 
        for j in range(i + 1, len(liste_arrondie)):  
            if liste_arrondie[i] > liste_arrondie[j]:
                liste_arrondie[i], liste_arrondie[j] = liste_arrondie[j], liste_arrondie[i]
    
    return liste_arrondie

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = arrondir_et_trier(L)
print("Liste après arrondi et tri dans l'ordre croissant :", resultat)
