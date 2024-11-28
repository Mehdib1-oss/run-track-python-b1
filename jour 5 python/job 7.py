def compter_multiples_de_3(liste):
    count = 0
    for element in liste:
        if element % 3 == 0:
            count += 1
    return count

L = [8, 24, 48, 2, 16]
resultat = compter_multiples_de_3(L)
print("Nombre de multiples de 3 dans la liste:", resultat)
