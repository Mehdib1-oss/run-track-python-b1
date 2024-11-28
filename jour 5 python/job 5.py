def modifier_case_voisine():
    L = [10, 20, 30, 40, 50]
    
    print("Deuxième valeur de la liste : ", L[1])
    
    L[3] = L[2] + L[4]
    
    print("Liste après modification : ", L)
    
    print("Dernière valeur de la liste : ", L[-1])

modifier_case_voisine()
