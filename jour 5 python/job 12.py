def trier_liste(liste):
    for i in range(len(liste) - 1):  
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:  
              
                liste[i], liste[j] = liste[j], liste[i]

L = [7, 11, 42, 39, 2]
trier_liste(L)
print("Liste triée dans l'ordre croissant :", L)
