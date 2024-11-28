def supprimer_doublons(liste):
    liste_sans_doublons = []
    
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    
    return liste_sans_doublons

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L_sans_doublons = supprimer_doublons(L)
print("Liste sans doublons :", L_sans_doublons)
